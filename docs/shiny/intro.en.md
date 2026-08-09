# R Shiny Quick Start Notes

## 0. Preface

### 0.1 What is this

These are R Shiny introductory learning notes. The goal is: **Master the complete process of building a basic data display application within a week**.

Instead of pursuing complexity, we first build a minimal application that is runnable and interpretable.

### 0.2 Why learn Shiny

- Data need to be repeatedly displayed in research, teaching or project reporting
- Hope to extend ggplot chart into an interactive interface
- Hope to mainly use R language to complete interactive data display
- Want to quickly build data display results in the form of web pages

### 0.3 What foundations are needed?

- Know basic R (just know how to install packages, write functions, and draw pictures)
- Ability to use R development environments such as RStudio or Positron
- Understand basic data frame, vector and plotting syntax

## 1. Learning plan (7-day learning path)

### Day 1: Hello World

**Goal:** Run the first Shiny App

**Things to learn:**

- Packed in Shiny bag
- UI and Server responsibilities
- How to run the App
- Basic input and output

**Note content:**

- The simplest example
- Common errors and solutions
- An example of a slider controlling a histogram

### Day 2: Layout and Theme

**Goal:** Make the App structure clearer and more visually unified

**Things to learn:**

- `sidebarLayout()` sidebar layout
- `tabPanel()` multi-tab page
- Basic HTML tags
- Set theme using `bslib` or `shinythemes`

**Note content:**

- Several common layouts
- How to add title and description text
- Change theme with one click

### Day 3: Various input controls

**Goal:** Learn to use various input boxes

**Things to learn:**

- `sliderInput()` Slider
- `selectInput()` drop-down box
- `checkboxInput()` checkbox
- `textInput()` text box
- `fileInput()` file upload

**Note content:**

- Examples of each type of control
- How to get the value entered by the user
- Practical combat: Make a data filter

### Day 4: Show results

**Goal:** Display the analysis results

**Things to learn:**

- `plotOutput()` display chart
- `tableOutput()` display form
- `textOutput()` display text
- `downloadHandler()` download function

**Note content:**

- ggplot2 chart display
- DT package for interactive forms
- How to let users download results

### Day 5: Reactive Programming Basics

**Goal:** Understand the core concepts of Shiny

**Things to learn:**

- The role of `reactive()`
- The difference between `observe()` and `observeEvent()`
- When to use what

**Note content:**

- Brief explanation of reaction formula
- Frequently asked questions and solutions
- Practical combat: linked drop-down box

### Day 6: Practical item

**Goal:** Make a complete small item

**item selection:**

1. **Data Exploration Tool**: Upload CSV and automatically generate statistical charts
2. **Simple Dashboard**: Display some key indicators and refresh regularly
3. **Data comparison tool**: Upload two files and compare the differences

**Note content:**

- Complete code
- Problems encountered and resolution process
- Areas that can be improved

### Day 7: Deployment and online

**Goal:** Make your app accessible to others

**Things to learn:**

- shinyapps.io Getting Started Deployment
- Local LAN sharing
- Package it for others to use

**Note content:**

- Account registration and deployment steps
- Common deployment errors
- Share the link with others

## 2. Resource organization

### 2.1 Required packages

```r
#Core
install.packages("shiny")

#Themes and Bootstrap styles
install.packages("bslib")

#More controls
install.packages("shinyWidgets")

#Interactive form
install.packages("DT")

#Interactive charts (optional)
install.packages("plotly")
```

### 2.2 Recommended resources

- **Official Tutorial**: https://shiny.posit.co/r/getstarted/shiny-basics/lesson1/
- **Control Display**: https://shiny.posit.co/r/gallery/widgets/widget-gallery/
- **Stack Overflow**: If you encounter a problem, search "shiny + your question"

### 2.3 Cheat Sheet

Most commonly used functions

**UI side:**

- `fluidPage()` - Create page
- `sidebarLayout()` - Sidebar layout
- `XXXInput()` - Various inputs
- `XXXOutput()` - various outputs

**Server side:**

- `renderPlot()` - Render chart
- `renderTable()` - Rendering table
- `reactive()` - Create reactive expressions
- `observe()` - Observe changes

## 3. Summary

### 3.1 Applicable objects

- Those who just want to get started quickly, give priority to completing the introductory practice
- There is a simple requirement to be realized
- Need to quickly complete data display prototypes
- Those who want to learn in the form of short tutorials

### 3.2 Not applicable objects

- For complex enterprise applications
- Pursuing best practices
- Need to understand the principles in depth
- To handle large-scale data

### 3.3 Learning Outcomes

- Data upload and display
- Simple interactive charts
- Basic data filtering and downloading
- Sufficient interface layout

Study suggestions

1. You will definitely encounter a lot of errors the first time, which is normal.
2. Start with the smallest runnable example and then gradually modify the parameters and structure
3. Don’t get hung up on the principles, complete the runnable examples first, and then gradually understand the principles.
4. When encountering problems, give priority to reading error messages, official documents and reproducible examples, and then consult the community Q&A

About examples

All examples are kept at an introductory scale, focusing on illustrating key concepts and modifiable code structures.

Okay, let’s get started! The goal on day one is to get a Shiny App running, and trust me, the barrier to entry is low!
