---
tags:
  - guide
share: true
title: Guide Dataview
---
## Standard Fields
status: string = TODO, IN_PROGRESS, DONE, CANCELLED, NON_TASK
priority: string = lowest, low, normal, medium, high, highest

## Dataview Basics
For active projects:
```
LIST
FROM "Projects" and #project and !#navigation
WHERE !completion AND status != "DONE" AND status != "CANCELLED"
SORT status, due
```

```
file.inlinks AS "Mentions"
```

```
\-
```
= date(2024-06-19T10:00) - date(2024-06-19T09:00)

### Inline Calculations
release-date:: 2027-06-18T12:00
```
\- until release!!
```
P2Y1MT11H37M0.621S until release!!

## DataviewJS

dv.date("now").toFormat("x");

### Rename, Move, AND Link To Main Page
```
<%* await app.vault.modify(tp.file.find_tfile(tp.file.path(true)), ""); _%>
<%*
let filename = tp.file.title;
if (filename.startsWith("Untitled")) {
	filename = await tp.system.prompt("Project Name [title]", "Project Title");
	filename = filename.replace(/[^a-zA-Z0-9\/]+/g, "_");
//	await tp.file.rename(filename);
};
const filepath = "Projects/" + tp.date.now("YYYY") + "/" + filename;
await tp.file.move(filepath + "/" + filename);
const tag = "#" + filepath;
_%>


// by https://forum.obsidian.md/u/flatline
// from https://forum.obsidian.md/t/whats-better-tags-at-the-end-of-text-or-tags-in-front-matter/55422/2

const pagesWithQuotes = await Promise.all(
	dv
	.pages("<% tag %>")
	.map(pageWithQuote => new Promise(async (resolve, reject) => {
		const content = await dv.io.load(pageWithQuote.file.path);
		resolve({
			link: pageWithQuote.file.link,
			content,
			modified: pageWithQuote.file.mtime
		});
	}))
);

// Create an array of pages containing quotes,
// where each page is:
// {
// quotes: [], // array of quotes
// link: { path: "" } // Link
// }

const quotesByPage = pagesWithQuotes.sort((a, b) => b.modified - a.modified).map(({
	link,
	content
}) => ({
	link,
	quotes: content
		// Split into paragraphs
		.split("# ")
		
		// Get only paragraphs that have the tag AND is not #timelog
		.filter(content => content.includes("<% tag %>") && !content.includes("#timelog"))
		
		// Remove the first tag from each quote string
		.map(content => content.replace("<% tag %>", "").replace(/\n/g,"\n> "))
}));
quotesByPage.forEach(
	page => 
	page.quotes.forEach(
		quote => dv.paragraph(`> [!note]- From ${page.link}${quote}`)
	)
);

const timelogByPage = pagesWithQuotes.sort((a, b) => b.modified - a.modified).map(({
	link,
	content
}) => ({
	link,
	quotes: content
		// Split into paragraphs
		.split("\n")
		
		// Get only paragraphs that have the tag AND #timelog
		.filter(content => content.includes("<% tag %>") && content.includes("#timelog"))
		
		// Remove the first tag from each quote string
		.map(content => content.replace("#timelog", "").replace("<% tag %>", ""))
}));
let timelog = "";
let timelogSum = {
	hours: 0,
	minutes: 0,
};
timelogByPage.forEach(
	page => 
	page.quotes.forEach(
		quote => {
			let regex = /date\(([^)]+)\)/g;
			let matches = [...quote.trim().slice(1, -1).matchAll(regex)];
			if (matches.length === 2) {
				let timelogDateEnd = matches[0][1];
			    let timelogDateStart = matches[1][1];
			    let timelogMinutes = Math.floor((dv.date(timelogDateEnd) - dv.date(timelogDateStart)) / (1000 * 60));
			    let timelogHours = Math.floor(timelogMinutes / 60);
			    timelogMinutes = timelogMinutes % 60;
				timelog += `> ${page.link}    |     ${String(timelogHours).padStart(2, '0')}:${String(timelogMinutes).padStart(2, '0')}\n`;
			    timelogSum.minutes += timelogMinutes;
			    timelogSum.hours += timelogHours;
			}
		}
	)
);

timelogSum.hours += Math.floor(timelogSum.minutes / 60);
timelogSum.minutes = timelogSum.minutes % 60;
dv.span(`> [!note]+ Timelog:\n> Total: ${timelogSum.hours} Hours, ${timelogSum.minutes} Minutes\n> \n${timelog}`)
```

### Resources

[Datavuew Functions](https://blacksmithgu.github.io/obsidian-dataview/reference/functions/)
[DataviewJS Functions](https://blacksmithgu.github.io/obsidian-dataview/api/code-reference/)
[How to achieve a hierarchical Dataview list without bullets but maintaining indentation](https://forum.obsidian.md/t/how-to-achieve-a-hierarchical-dataview-list-without-bullets-but-maintaining-indentation/66011)
