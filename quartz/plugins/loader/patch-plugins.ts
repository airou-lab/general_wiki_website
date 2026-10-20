import fs from "fs"
import path from "path"

export function patchPlugins(): void {
  const root = process.cwd()

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
