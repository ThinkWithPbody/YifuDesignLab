---
share: true
tags:
  - guide
---

[Markdown Cheatsheet](https://rentry.org/how)

# Heading 1

## Heading 2

### Heading 3

#### Heading 4

##### Heading 5

###### Heading 6

## Styles

Body
**Bold**
*Italic*
~~Strikethrough~~

## Formats

- Bullet Point
- Bullet Point
	- Nested Bullet Point
1. Numbered List
2. Numbered List
	1. Nested Numbered List
- [x] Checkbox [completion:: 2024-01-01]
- [p] Pro
- [c] Con
- [I] Idea
	Reason

> Quote
> Multi line

This[^1] is a simple[^2] footnote.[^3]

Break Line

___

## Callouts

> [!white] Default Callouts
>
> > [!note]
>
> > [!quote]
>
> > [!info]
>
> > [!question]
>
> > [!success]
>
> > [!failure]
>
> > [!warning]
>
> > [!danger]
>
> > [!todo]
>
> > [!important]
>
> > [!abstract]
>
> > [!example]

> [!white] Custom Callouts
>
> > [!white]
>
> > [!grey]
>
> > [!black]
>
> > [!blue]
>
> > [!yellow]
>
> > [!pink]
>
> > [!green]

## References

Reference to a [File](./index.md)
Reference to a [Heading](Obsidian.md#heading-1)
Reference to a [Paragraph](../../2024-01-01.md#025433)
Inline Reference![Guides/Obsidian > Styles](Obsidian.md#styles)

## Latex

| Meaning        | Symbol | LaTeX Command   |
| -------------- | ------ | --------------- |
| Therefore      | ∴      | \therefore      |
| Because        | ∵      | \because        |
| Implies        | ⇒      | \Rightarrow     |
| If and only if | ⇔      | \Leftrightarrow |
| For all        | ∀      | \forall         |
| Exists         | ∃      | \exists         |
| Not Exists     | ∄      | \nexists        |
| Logical AND    | ∧      | \land           |
| Logical OR     | ∨      | \lor            |
| Negation (Not) | ¬      | \neg            |

## Shortcuts

### View

Ctrl = Enable Hover Preview On Links
Ctrl + E = Toggle Source Mode
Ctrl + R = Toggle Reading Mode
Alt + R = Reveal File In Navigation

### Edit

Alt = [Multiple Cursors](https://help.obsidian.md/Editing+and+formatting/Multiple+cursors)
Alt + C = Format Callout
Alt + T = Modify Task
Alt + A = Emoji Toolbar
Ctrl + Drag + Drop = Embed / Transclude

### Format

Alt + Q = QuickAdd
Alt + E = Templater

### Excalidraw

Alt + D = Excalidraw Deconstruct Selected
Alt + F = Excalidraw Toggle Back of Note
Alt + B = Excalidraw Show Selected Back of Note

[^1]: This is the referenced text.
[^2]: Add 2 spaces at the start of each new line.
  This lets you write footnotes that span multiple lines.
  Referenced footnote will appear at the bottom of the page in Reading View.
[^3]: Named footnotes still appear as numbers, but can make it easier to identify and link references.
