---
share: true
tags:
  - guide
---

## Date

[Date Module](https://silentvoid13.github.io/Templater/internal-functions/internal-modules/date-module.html)
[ISO 8601 Durations](https://en.wikipedia.org/wiki/ISO_8601#Durations)
[moment.js String Format](https://momentjs.com/docs/#/parsing/string-format/)

## Examples

[Templates Showcase](https://github.com/SilentVoid13/Templater/discussions/categories/templates-showcase)
[zachyoung Templater snippets](https://zachyoung.dev/posts/templater-snippets)
[Christian's Templater Templates](https://github.com/chhoumann/Templater_Templates)

## Templates

`<% tp.file.cursor() %>`

### Rename Move

```
<%*
let filename = tp.file.title;
if (filename.startsWith("Untitled")) {
	filename = await tp.system.prompt("Course Title [code-title]", "ARC0000Y-Course Title");
	filename = filename.replace(/[^a-zA-Z0-9\/-]+/g, "_");
	await tp.file.rename(filename);
};
await new Promise(resolve => setTimeout(resolve, 1000));
const filepath = "Courses/" + tp.date.now("YYYY") + "/" + filename;
await tp.file.move(filepath + "/" + filename);
await tp.file.rename(filename);
const tag = "#" + filepath;

let words = await filename.split("-");
let code = words[0];
let title = words.slice(1).join("-");
_%>
```

### File Link Display

```
`<%*
const fileName = "This is the name of a file";
const existing = tp.file.find_tfile(fileName);
let createdFileDisplay;
if (existing) {
  createdFileDisplay = existing.basename;
} else {
  createdFileDisplay = (await tp.file.create_new(tp.file.find_tfile("template-name"), fileName)).basename;
}
_%>`
```

`[[<% createdFileDisplay %>]]`

### Yearly Tasks

```
<%*
const lastMonthOfYear = tp.date.now("YYYY-MM-DD", "P1Y-1M", tp.file.title, "YYYY");

let currentMonth = tp.date.now("YYYY-MM-DD", 0, tp.file.title, "YYYY");
while (currentMonth <= lastMonthOfYear) {
	let currentMonthNum = tp.date.now("MM", 0, currentMonth, "YYYY-MM-DD")
	if ( (currentMonthNum - 1) % 3 == 0) {
	// Quarterly
	_%>
### Q<% Math.floor(currentMonthNum / 3) + 1 %>
- [ ] Pay Parking: <% tp.date.now("YYYY MMM", "P3M", currentMonth, "YYYY-MM-DD") %> - <% tp.date.now("MMM", "P5M", currentMonth, "YYYY-MM-DD") %> [due:: <% tp.date.now("YYYY-MM-DD", "P3M-1W", currentMonth, "YYYY-MM-DD") %>] [start:: <% tp.date.now("YYYY-MM-DD", "P3M-2W", currentMonth, "YYYY-MM-DD") %>]
<%*
	}
	// Monthly
_%>
#### <% tp.date.now("MMMM", 0, currentMonth, "YYYY-MM-DD")%>
- [ ] Pay Rent: <% tp.date.now("YYYY MMMM", "P1M", currentMonth, "YYYY-MM-DD") %>  [due:: <% tp.date.now("YYYY-MM-DD", "P1M", currentMonth, "YYYY-MM-DD") %>] [start:: <% tp.date.now("YYYY-MM-DD", "P1M-1W", currentMonth, "YYYY-MM-DD") %>]
<%*
	let lastDayOfMonth = tp.date.now("YYYY-MM-DD", "P1M-1D", currentMonth, "YYYY-MM-DD");
	let mondays = [];
	let currentDay = tp.date.now("YYYY-MM-DD", 0, currentMonth, "YYYY-MM-DD");
	let foundFirstMonday = false;
	
	while (currentDay <= lastDayOfMonth) {
		let dayOfWeek = tp.date.now("E", 0, currentDay, "YYYY-MM-DD");
		
		if (foundFirstMonday) {
			mondays.push(currentDay);
			currentDay = tp.date.now("YYYY-MM-DD", 7, currentDay, "YYYY-MM-DD");
			} else if (!foundFirstMonday && dayOfWeek === "1") {
			mondays.push(currentDay);
			foundFirstMonday = true;
			currentDay = tp.date.now("YYYY-MM-DD", 7, currentDay, "YYYY-MM-DD");
			} else {
			currentDay = tp.date.now("YYYY-MM-DD", 1, currentDay, "YYYY-MM-DD");
		}
	}
	
	for (let monday of mondays) { 
	// Weekly
_%>
- [ ] Check TD My Advantage [due:: <% tp.date.now("YYYY-MM-DD", "P-1D", monday, "YYYY-MM-DD") %>] [start:: <% tp.date.now("YYYY-MM-DD", "P-2D", monday, "YYYY-MM-DD") %>]
<%* }
	
	currentMonth = tp.date.now("YYYY-MM-DD", "P1M", currentMonth, "YYYY-MM-DD");
}
_%>
```
