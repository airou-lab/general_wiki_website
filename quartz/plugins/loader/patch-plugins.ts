import fs from "fs"
import path from "path"

export function patchPlugins(): void {
  const root = process.cwd()

  // 1. Patch graph plugins (permanent visible edges & current page centering)
  const graphFiles = [
    path.join(root, "node_modules/@quartz-community/graph/dist/index.js"),
    path.join(root, "node_modules/@quartz-community/graph/dist/components/index.js"),
    path.join(root, ".quartz/plugins/graph/dist/index.js"),
    path.join(root, ".quartz/plugins/graph/dist/components/index.js"),
  ]

  for (const file of graphFiles) {
    if (fs.existsSync(file)) {
      let code = fs.readFileSync(file, "utf-8")

      // Add de = --darkgray to color resolution in bundled JS
      if (
        !code.includes(
          'var Y=getComputedStyle(document.documentElement),de=h(Y.getPropertyValue("--darkgray").trim(),"#4e4e4e"),',
        )
      ) {
        code = code.replace(
          'var Y=getComputedStyle(document.documentElement),Ie=h(Y.getPropertyValue("--secondary").trim(),"#c792ea"),',
          'var Y=getComputedStyle(document.documentElement),de=h(Y.getPropertyValue("--darkgray").trim(),"#4e4e4e"),Ie=h(Y.getPropertyValue("--secondary").trim(),"#c792ea"),',
        )
      }

      // Update Ve() in bundled JS to use de (--darkgray) idempotently
      code = code.replace(
        /function Ve\(\)\{[\s\S]*?function qe\(\)/,
        "function Ve(){for(var i=0;i<z.length;i++){var l=z[i];if(_u!==null){l.active?(l.alpha=1,l.width=2.5,l.color=Ie):(l.alpha=.1,l.width=1,l.color=de)}else{l.alpha=.55,l.width=1.5,l.color=de}}}function qe()",
      )

      // Stroke width and alpha in bundled JS
      code = code.replace(
        "v.gfx.stroke({alpha:v.alpha,width:1,color:v.color})",
        "v.gfx.stroke({alpha:v.alpha,width:v.width||1.5,color:v.color})",
      )
      code = code.replace(
        "v.gfx.stroke({alpha:v.alpha*0.75,width:1.5,color:v.color})",
        "v.gfx.stroke({alpha:v.alpha,width:v.width||1.5,color:v.color})",
      )
      code = code.replace("color:te,alpha:1,active:!1", "color:de,width:1.5,alpha:.55,active:!1")
      code = code.replace("color:ee,alpha:1,active:!1", "color:de,width:1.5,alpha:.55,active:!1")
      code = code.replace("color:ee,width:1.5,alpha:.65,active:!1", "color:de,width:1.5,alpha:.55,active:!1")

      // Center current node in local graph (fx=0, fy=0)
      code = code.replace(
        /v=\{id:i,text:F,tags:A,x:[\s\S]*?vx:0,vy:0\};[\s\S]*?nu\.push\(v\),ju\.set\(i,v\)/,
        "v={id:i,text:F,tags:A,x:i===m?0:(Math.random()-.5)*(R*.5),y:i===m?0:(Math.random()-.5)*(O*.5),vx:0,vy:0};if(i===m&&Vu>=0){v.fx=0;v.fy=0}nu.push(v),ju.set(i,v)",
      )

      // Center camera on current node in global graph idempotently
      code = code.replace(
        /a\.select\(Z\.canvas\)\.call\(et\)[\s\S]*?var se=!1;/,
        "a.select(Z.canvas).call(et);var cur=ju.get(m);if(cur&&Vu<0){au.tick(35);var ix=R/2-qu*(cur.x+R/2),iy=O/2-qu*(cur.y+O/2);P=a.zoomIdentity.translate(ix,iy).scale(qu);a.select(Z.canvas).call(et.transform,P)}}var se=!1;",
      )

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

  const searchTargetNew =
    ';!S.tags.some(x=>x.toLowerCase()===\"archive\")&&(Nt.sort((a,b)=>{let sa=Ht[a]||\"\",sb=Ht[b]||\"\";let aa=sa.startsWith(\"archived_material/\")||sa.includes(\"/archived_material/\")||(Z?.[sa]?.tags||[]).some(t=>t.toLowerCase()===\"archive\")?1:0;let bb=sb.startsWith(\"archived_material/\")||sb.includes(\"/archived_material/\")||(Z?.[sb]?.tags||[]).some(t=>t.toLowerCase()===\"archive\")?1:0;return aa-bb}));let ft=S.query||(S.tags.length>0?S.tags.join(\" \"):E),he=Nt.map(at=>Bi(ft,at));await z(he.slice(0,kn));'

  const searchLimitOld = 'limit:S.tags.length>0?1e4:kn,index:["title","content"]'
  const searchLimitNew = 'limit:1e4,index:["title","content"]'

  for (const file of searchFiles) {
    if (fs.existsSync(file)) {
      let code = fs.readFileSync(file, "utf-8")
      code = code.replace(
        /([,;]!S\.tags\.some[\s\S]*?|[,;]ft=S\.query[\s\S]*?)await z\(he\.slice\(0,kn\)\);/,
        searchTargetNew,
      )
      if (code.includes(searchLimitOld)) {
        code = code.replace(searchLimitOld, searchLimitNew)
      }
      fs.writeFileSync(file, code, "utf-8")
    }
  }
}
