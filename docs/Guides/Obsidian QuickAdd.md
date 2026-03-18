---
share: true
tags:
  - guide
---

### +timelog

Copy the following tag options

[#Projects/2024/Yifu_Design_Lab](#Projects/2024/Yifu_Design_Lab),#Courses/2026/ARC3405HS,#Courses/2026/ARC3021Y,#Courses/2026/ARC3052H,#Projects/Job_Hunt,#Projects/2026/ARC3405HS_Project-01

And insert behind `{{VALUE:`

```
 #timelog {{VALUE:}} \n
```

Then, under Quick Add plugin settings, use the entirety of this modified string as the **Capture Format** for **+timelog** > Macro **3: Add Tags**

### Case Transforms for VALUE/NAME

Use the new `|case:<style>` pipe syntax to transform any VALUE or NAME token inline — no extra variables or macros needed. Eight styles are supported:

|Style|Example|
|---|---|
|`kebab`|`my-new-blog`|
|`snake`|`my_new_blog`|
|`camel`|`myNewBlog`|
|`pascal`|`MyNewBlog`|
|`title`|`My New Blog`|
|`lower`|`my new blog`|
|`upper`|`MY NEW BLOG`|
|`slug`|`my-new-blog` (filename-safe)|

Combine with other options freely: `{{VALUE:title|label:Post Title|case:kebab}}`. Each token applies its own transform independently, so you can reuse the same variable with different casing in a single template — for example, `{{VALUE:title}}` for the heading and `{{VALUE:title|case:slug}}` for the filename. Autocomplete suggestions appear as you type `|case:`. ([#1103](https://github.com/chhoumann/quickadd/pull/1103))