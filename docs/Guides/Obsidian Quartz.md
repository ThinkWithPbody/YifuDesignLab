---
share: true
tags:
  - guide
date: 2025-02-20
---

### Explorer

I use the following settings to hide notes with any tag, and notes with the frontmatter hide: true along with their parent folder. If a folder has only one file, that folder is renamed and linked to the note instead, hiding the original file from the Explorer.

`quartz.layout.ts`

```
Component.Explorer({
            folderClickBehavior: "link",
            folderDefaultState: "open",

            filterFn: (node) => {
                // Hide files with hide: true
                if (node.file?.frontmatter?.tags?.includes("badtag")) {
                    return false;
                }

                if (node.file?.frontmatter?.hide === true) {
                    return false;
                }
                // Hide folders with a single hidden file
                if (node.children?.length === 1 && node.children[0].file?.frontmatter?.hide === true) {
                    return false;
                }
                return true;
            },
            mapFn: (node) => {
                if (node.children?.length === 1 &&
                    node.children[0].file &&
                    node.name === node.children[0].name.replace(/\.md$/, '')) {
                    node.file = node.children[0].file;
                    node.displayName = node.children[0].displayName;
                    node.children = [];
                }
                return node;
            },
        }),
```
