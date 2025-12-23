I recommend using [Obsidian](https://obsidian.md/) to edit this vault as [quartz4](https://quartz.jzhao.xyz/) is built for this. Simply create a new vault in the `contents` folder of the repo and start editing.

# Quartz4
- To place a note at a folder's index, create the note name as `index`
- To rename the file's title, use the metadata tag `title: {your title}`
- use `[[yourFile]]` to link a file, obsidan should auto complete this smartly (you can type the folder name and it can bring up the `index` file)
- see the quartz4 docs for more info!

# Deploying
Deploy locally:
```bash
npx quartz build --serve
```
Deploy to prod (required to have push permissions):
```bash
npx quartz sync
```
However, if you'er using the obsidan vault, you can manually push and commit via the command pallet (crntl +p -> "Git: Push"). 