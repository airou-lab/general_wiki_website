import fs from "fs"
import path from "path"

export function patchPlugins(): void {
  const root = process.cwd()

  // 1. Patch graph plugins (permanent visible edges, focal link highlight & visible neighbor labels)
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

      // Update Wu(), Ve(), qe(), Ke(), Au() to highlight focal node connections and neighbor labels at resting state
      const replacementWuAu =
        "function Wu(i){_u=i;var target=i||m;iu=new Set;if(target){iu.add(target);for(var l=0;l<z.length;l++){var F=z[l].simulationData;F.source.id===target||F.target.id===target?(iu.add(F.source.id),iu.add(F.target.id),z[l].active=!0):z[l].active=!1}for(var l=0;l<L.length;l++)L[l].active=iu.has(L[l].simulationData.id)}else{for(var l=0;l<L.length;l++)L[l].active=!1;for(var l=0;l<z.length;l++)z[l].active=!1}}function Ve(){for(var i=0;i<z.length;i++){var l=z[i];if(_u!==null){l.active?(l.alpha=1,l.width=2.5,l.color=Ie):(l.alpha=.15,l.width=1,l.color=de)}else{l.active?(l.alpha=1,l.width=2.2,l.color=Ie):(l.alpha=.55,l.width=1.4,l.color=de)}}}function qe(){for(var i=1/qu,l=i*1.15,F=0;F<L.length;F++){var A=L[F];if(_u!==null){_u===A.simulationData.id?(A.label.alpha=1,A.label.scale.set(l)):A.active?(A.label.alpha=.85,A.label.scale.set(i)):(A.label.alpha=0,A.label.scale.set(i))}else{A.simulationData.id===m?(A.label.alpha=1,A.label.scale.set(l)):A.active?(A.label.alpha=.85,A.label.scale.set(i)):(A.label.alpha=0,A.label.scale.set(i))}}}function Ke(){for(var i=0;i<L.length;i++){var l=L[i],F=1;_u!==null&&(F=l.active?1:.25);l.gfx.alpha=F}}function Au(){Ke(),Ve(),qe()}"

      code = code.replace(/function Wu\(i\)\{[\s\S]*?function Au\(\)\{[\s\S]*?\}/, replacementWuAu)

      // Ensure resting state initialization
      if (!code.includes("Wu(null),Au(),ce()")) {
        code = code.replace("Au(),ce()", "Wu(null),Au(),ce()")
      }

      // Stroke width and alpha in bundled JS
      code = code.replace(
        "v.gfx.stroke({alpha:v.alpha,width:1,color:v.color})",
        "v.gfx.stroke({alpha:v.alpha,width:v.width||1.4,color:v.color})",
      )
      code = code.replace("color:te,alpha:1,active:!1", "color:de,width:1.4,alpha:.55,active:!1")

      // Center current node in local graph (fx=0, fy=0)
      code = code.replace(
        /v=\{id:i,text:F,tags:A,x:[\s\S]*?vx:0,vy:0\};[\s\S]*?nu\.push\(v\),ju\.set\(i,v\)/,
        "var ic=i===m;v={id:i,text:F,tags:A,x:ic?0:(Math.random()-.5)*(R*.5),y:ic?0:(Math.random()-.5)*(O*.5),vx:0,vy:0};if(ic&&Vu>=0){v.fx=0;v.fy=0}nu.push(v),ju.set(i,v)",
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
