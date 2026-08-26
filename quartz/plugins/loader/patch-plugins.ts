import fs from "fs"
import path from "path"

export function patchPlugins(): void {
  const root = process.cwd()

  // 1. Patch graph plugins (permanent visible edges)
  const graphFiles = [
    path.join(root, "node_modules/@quartz-community/graph/dist/index.js"),
    path.join(root, "node_modules/@quartz-community/graph/dist/components/index.js"),
    path.join(root, ".quartz/plugins/graph/dist/index.js"),
    path.join(root, ".quartz/plugins/graph/dist/components/index.js"),
    path.join(root, ".quartz/plugins/graph/src/components/scripts/graph.inline.ts"),
  ]

  for (const file of graphFiles) {
    if (fs.existsSync(file)) {
      let code = fs.readFileSync(file, "utf-8")

      // In src / TS:
      code = code.replace(
        /function renderLinks\(\) \{[\s\S]*?linkData\.color = linkData\.active \? gray : lightgray;[\s\S]*?\}/,
        `function renderLinks() {
        for (var i = 0; i < linkRenderData.length; i++) {
          var linkData = linkRenderData[i];
          if (hoveredNodeId !== null) {
            if (linkData.active) {
              linkData.alpha = 1.0;
              linkData.width = 2.5;
              linkData.color = secondary;
            } else {
              linkData.alpha = 0.12;
              linkData.width = 1.0;
              linkData.color = gray;
            }
          } else {
            linkData.alpha = 0.65;
            linkData.width = 1.5;
            linkData.color = gray;
          }
        }
      }`,
      )

      // In bundled JS:
      code = code.replace(
        "function Ve(){for(var i=0;i<z.length;i++){var l=z[i],F=1;_u!==null&&(F=l.active?1:.2),l.alpha=F,l.color=l.active?ee:te}}",
        "function Ve(){for(var i=0;i<z.length;i++){var l=z[i];if(_u!==null){l.active?(l.alpha=1,l.width=2.5,l.color=Ie):(l.alpha=.12,l.width=1,l.color=ee)}else{l.alpha=.65,l.width=1.5,l.color=ee}}}",
      )
      code = code.replace(
        "function Ve(){for(var i=0;i<z.length;i++){var l=z[i],F=1;_u!==null&&(F=l.active?1:.2),l.alpha=F,l.color=l.active?Ie:ee}}",
        "function Ve(){for(var i=0;i<z.length;i++){var l=z[i];if(_u!==null){l.active?(l.alpha=1,l.width=2.5,l.color=Ie):(l.alpha=.12,l.width=1,l.color=ee)}else{l.alpha=.65,l.width=1.5,l.color=ee}}}",
      )
      code = code.replace(
        "v.gfx.stroke({alpha:v.alpha,width:1,color:v.color})",
        "v.gfx.stroke({alpha:v.alpha,width:v.width||1.5,color:v.color})",
      )
      code = code.replace(
        "v.gfx.stroke({alpha:v.alpha*0.75,width:1.5,color:v.color})",
        "v.gfx.stroke({alpha:v.alpha,width:v.width||1.5,color:v.color})",
      )
      code = code.replace("color:te,alpha:1,active:!1", "color:ee,width:1.5,alpha:.65,active:!1")
      code = code.replace("color:ee,alpha:1,active:!1", "color:ee,width:1.5,alpha:.65,active:!1")

      fs.writeFileSync(file, code, "utf-8")
    }
  }

  // 2. Patch search plugins (downweight archive)
  const searchFiles = [
    path.join(root, "node_modules/@quartz-community/search/dist/index.js"),
    path.join(root, "node_modules/@quartz-community/search/dist/components/index.js"),
    path.join(root, ".quartz/plugins/search/dist/index.js"),
    path.join(root, ".quartz/plugins/search/dist/components/index.js"),
  ]

  const searchTargetOld =
    'ft=S.query||(S.tags.length>0?S.tags.join(" "):E),he=Nt.map(at=>Bi(ft,at));await z(he.slice(0,kn));'
  const searchTargetNew =
    'if(!S.tags.some(x=>x.toLowerCase()==="archive")){Nt.sort((a,b)=>{let sa=Ht[a]||"",sb=Ht[b]||"";let aa=sa.startsWith("archived_material/")||sa.includes("/archived_material/")||(Z?.[sa]?.tags||[]).some(t=>t.toLowerCase()==="archive")?1:0;let bb=sb.startsWith("archived_material/")||sb.includes("/archived_material/")||(Z?.[sb]?.tags||[]).some(t=>t.toLowerCase()==="archive")?1:0;return aa-bb})};ft=S.query||(S.tags.length>0?S.tags.join(" "):E),he=Nt.map(at=>Bi(ft,at));await z(he.slice(0,kn));'
  const searchLimitOld = 'limit:S.tags.length>0?1e4:kn,index:["title","content"]'
  const searchLimitNew = 'limit:1e4,index:["title","content"]'

  for (const file of searchFiles) {
    if (fs.existsSync(file)) {
      let code = fs.readFileSync(file, "utf-8")
      if (code.includes(searchTargetOld)) {
        code = code.replace(searchTargetOld, searchTargetNew)
      }
      if (code.includes(searchLimitOld)) {
        code = code.replace(searchLimitOld, searchLimitNew)
      }
      fs.writeFileSync(file, code, "utf-8")
    }
  }
}
