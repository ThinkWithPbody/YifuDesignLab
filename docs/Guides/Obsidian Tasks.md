---
share: true
tags:
  - guide
---

[Guide](https://publish.obsidian.md/tasks/Introduction)

[Filters](https://publish.obsidian.md/tasks/Queries/Filters)
[RegEx](https://publish.obsidian.md/tasks/Queries/Regular+Expressions)

### Default Filter

```
NOT done
starts before tomorrow
short mode
sort by priority
sort by status.type
description regex does not match /^$/
NOT (path includes Templater)
NOT (tag includes HideFromTasks)
```

### Tasks Page Dataview Setup

```
%%[parent:: [[index]]]%%

> [!blue]+ Active Projects
>  - [[Projects/2024/Yifu Design Lab/Yifu Design Lab.md|Yifu Design Lab]]
> - [[Courses/2025/ARC2014Y/ARC2014Y.md|ARC2014Y]]
> 

> [!yellow]+ Due
> ```tasks
> has due date
> (scheduled before next 2 week) OR (no scheduled date)
> ```

> [!pink]+ Scheduled
> ```tasks
> no due date
> scheduled before next 2 week OR no scheduled date
> NOT (tag includes shopping)
> ```

> [!green]+ Shopping
> ```tasks
> tag includes shopping
> ```

```
