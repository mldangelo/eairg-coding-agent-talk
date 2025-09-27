# Slidev Presentation Instructions

## Overview

Your talk has been converted to a fully-featured Slidev presentation with:

- **14 main slides** plus cover, discussion, references, and thank you slides
- **Interactive elements**: Click animations, hover effects, navigation
- **Rich visualizations**: Mermaid diagrams, mathematical notation, styled layouts
- **Professional styling**: Grid layouts, color-coded sections, responsive design

## Key Features Added

### 1. **Slide Layouts**

- `cover` - Title slide with background and navigation
- `default` - Standard content slides
- `two-cols` - Side-by-side comparisons
- `center` - Focused discussion slides
- `end` - Thank you slide

### 2. **Interactive Elements**

- `<v-clicks>` - Progressive revelation of content
- Hover effects on navigation elements
- Click-to-advance functionality

### 3. **Visual Enhancements**

- **Mermaid diagrams** for system architecture, agentic loops, and multi-agent workflows
- **Mathematical notation** using LaTeX syntax
- **Color-coded sections** with semantic backgrounds
- **Grid layouts** for organized content presentation

### 4. **Presenter Features**

- **Speaker notes** in HTML comments (`<!-- -->`)
- **Progressive disclosure** to control information flow
- **Visual hierarchy** with proper typography and spacing

## Running the Presentation

### Prerequisites

```bash
npm install -g @slidev/cli
```

### Start Development Server

```bash
cd /path/to/eairg-agent-talk
slidev talk.md
```

### Export Options

```bash
# Export to PDF
slidev export talk.md

# Export to PowerPoint
slidev export talk.md --format pptx

# Build static site
slidev build talk.md
```

## Customization Options

### Themes

The presentation uses the `academic` theme. You can change it in the frontmatter:

```yaml
theme: default # or seriph, apple, etc.
```

### Background Images

Add images to `./images/` directory and reference in frontmatter:

```yaml
background: ./images/your-background.jpg
```

### Transitions

Current transition is `slide-left`. Options include:

- `slide-up`, `slide-down`, `slide-right`
- `fade`, `zoom`

## Slide Structure

1. **Cover** - Title and introduction
2. **Research Landscape** - Current state of field
3. **Paradigm Shift** - From autocomplete to agents
4. **System Architecture** - Six core components
5. **Capabilities/Limitations** - What works vs. fails
6. **Alignment in Practice** - Real-world challenges
7. **Speed vs. Intelligence** - Model routing trade-offs
8. **Evaluation Crisis** - Benchmark limitations
9. **Multi-Agent Systems** - Collaboration patterns
10. **Security Challenges** - Safety research
11. **Future Directions** - Research roadmap
12. **Discussion Questions** - Interactive session
13. **Recommended Readings** - Resources
14. **Thank You** - Closing

## Tips for Presentation

1. **Use progressive clicks** - Content reveals step by step
2. **Refer to diagrams** - Visual aids support key concepts
3. **Engage with discussion questions** - Built-in interaction points
4. **Use speaker notes** - Guidance provided in comments
5. **Leverage animations** - Smooth transitions between concepts

## Troubleshooting

### Common Issues

- **Missing diagrams**: Ensure Mermaid is properly installed
- **LaTeX not rendering**: Check mathematical notation syntax
- **Layout issues**: Verify grid class names and structure

### Performance

- **Large presentations**: Consider splitting into multiple files
- **Image optimization**: Compress background images for faster loading

The presentation is now ready for your PhD seminar with professional-quality visuals and interactive features that will engage your academic audience!
