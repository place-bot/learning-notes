# Day 2: Layout and Theme - Make your app structure clearer

## 1. Review yesterday’s content first.

### 1.1 List of functions learned yesterday

First, sort out the functions used in the previous section and clarify the role of each parameter:

#### UI side function

**1. actionButton() - Create button**

```text
actionButton(inputId = "button1", # ID, give this button a name
             label = "Run Example") # The text displayed on the button
```

**2. sliderInput() - Create a slider**

```text
sliderInput(inputId = "slider1", # ID, the name of the slider
            label = "Select a number:", # Description text above the slider
            min = 1, # minimum value
            max = 100, # maximum value
            value = 50) #Default value
```

**3. textInput() - Create a text input box**

```text
textInput(inputId = "text1", # ID, the name of the input box
          label = "Please enter text:", # Description above the input box
          value = "") #Default value (optional)
```

**4. textOutput() - Display the position of the text**

```text
textOutput(outputId = "output1") # ID, which must correspond to the server
```

**5. plotOutput() - Display the position of the graph**

```text
plotOutput(outputId = "plot1", # ID must correspond to the server
           width = "100%", # Width (optional)
           height = "400px") # Height (optional)
```

#### Server side function

**1. renderText() - generate text output**

```r
output$output1 <- renderText({
  #Enter the text you want to display here.
  "Hello World"
})
```

**2. renderPlot() - generate graphical output**

```r
output$plot1 <- renderPlot({
  #Write the code for drawing pictures here.
  plot(1:10)
})
```

**3. observeEvent() - listen for events**

```r
#Example: Listen to the click of the button, and update the content of text1 after clicking.
observeEvent(
  input$button1,        #(1) Monitor which input - the number of times the user clicks input$button1
  {                      #(2) What to do when the event occurs
    output$text1 <- renderText({
      "You clicked the button!"
    })
  }
)
```

### 1.2 Rules for using brackets, quotation marks, and commas

This part is super important! Many errors occur because these symbols are used incorrectly.

#### Rules for parentheses ()

```text
# Rule 1: Function calls must have parentheses
sliderInput() # Right
sliderInput # Wrong!

# Rule 2: Parameters are written in parentheses and separated by commas
sliderInput("id1", "label", 1, 100, 50) # Right
sliderInput "id1" "label" 1 100 50 # Wrong!

# Rule 3: Parentheses should be paired
sliderInput( # start
  "id1",
  "label"
) # End, must correspond to
```

#### Rules for braces {}

```r
#Rule 1: Flower brackets are used to contain multi-line code.
server <- function(input, output) {    #Start
  #You can write a lot of lines of code.
  output$text1 <- renderText({
    "Hello"
  })
}                                      #End

#Rule 2: There must be curly brackets in the renderXXX function.
renderText({         #Yes, that's right.
  "Hello"
})

renderText("Hello")  #Wrong! Even if it's only one line, you should use parentheses.
```

#### Rules for quotation marks

```text
# Rule 1: All IDs must be quoted
sliderInput("slider1", ...) # Right
sliderInput(slider1, ...) # Wrong!

# Rule 2: All displayed text must be quoted.
"Choose a number:" # Right
Choose a number: # Wrong!

# Rule 3: Numbers do not need to be quoted.
min = 1 # Right
min = "1" # Can be used but not recommended

# Rule 4: No quotes after input$ and output$
input$slider1 # Right
input$"slider1" # Wrong!
```

#### Comma Rules

```r
#Rule 1: Function parameters are separated by commas.
sliderInput("id", "label", 1, 100, 50)  #Yes, that's right.

#Rule 2: There should be no comma after the last parameter.
sliderInput(
  "id",
  "label",
  1,
  100,
  50      #The last one, don't put a comma.
)

#Rule 3: Elements in the list should also be separated by commas.
fluidPage(
  h1("heading"),           #Need a comma
  p("paragraph"),            #Need a comma
  sliderInput(...)      #Don't put a comma at the end of the last one.
)
```

### 1.3 Common nested structures

Shiny code often has many levels of nesting. Let’s see how to understand it:

```r
#Layer 1: The entire app
shinyApp(
  #Second layer: UI definition
  ui = fluidPage(
    #Third layer: layout
    sidebarLayout(
      #Fourth layer: sidebar
      sidebarPanel(
        #Fifth layer: specific controls
        sliderInput("id", "label", 1, 100, 50)
      ),
      #Fourth layer: main panel
      mainPanel(
        #Fifth layer: output
        plotOutput("plot")
      )
    )
  ),
  #Second layer: Server definition
  server = function(input, output) {
    #Third layer: output definition
    output$plot <- renderPlot({
      #Fourth layer: specific code
      plot(1:10)
    })
  }
)
```

Indentation Tips

For each level you go deeper, indent 2 more spaces.
This way the code structure is clear at a glance

## 2. Layout basics: keep the app organized

### 2.1 The simplest layout: fluidPage

Yesterday we used `fluidPage()`, which is the most basic layout:

```r
library(shiny)

ui <- fluidPage(
  h1("This is the title."),
  p("This is the first paragraph."),
  p("This is the second paragraph."),
  sliderInput("slider", "Slider", 1, 100, 50),
  plotOutput("plot")
)

server <- function(input, output) {
  output$plot <- renderPlot({
    plot(1:input$slider)
  })
}

shinyApp(ui = ui, server = server)
```

Problem: Everything is piled together and the information hierarchy is not clear.

### 2.2 Sidebar layout: sidebarLayout

This is the most commonly used layout, with controls on the left and results on the right:

```r
library(shiny)

ui <- fluidPage(
  #Add a title
  titlePanel("My data analysis App"),

  #Sidebar layout
  sidebarLayout(
    #Left side: Put the controls.
    sidebarPanel(
      h3("control panel"),
      sliderInput("num", "Select the number of data points:",
                  min = 10,
                  max = 100,
                  value = 50),

      br(),  #Empty flight

      selectInput("color", "Choose the color:",
                  choices = c("red" = "red",
                              "blue" = "blue",
                              "green" = "green"),
                  selected = "blue")
    ),

    #Right side: output
    mainPanel(
      h3("Analysis results"),
      plotOutput("scatter")
    )
  )
)

server <- function(input, output) {
  output$scatter <- renderPlot({
    #Generate random data
    x <- rnorm(input$num)
    y <- rnorm(input$num)

    #Draw a scatter plot
    plot(x, y,
         col = input$color,
         pch = 19,
         main = paste("Scatter plot (", input$num, "A point)"))
  })
}

shinyApp(ui = ui, server = server)
```

- `fluidPage(...)`
  Create a top-level container for a responsive web layout. All UI elements should be placed here.
- `titlePanel(title)`
  Insert an app title at the top of the page. The parameter `title` is a string.
- `sidebarLayout(sidebar, main)`
  Define a row and two column layout: `sidebarPanel()` on the left and `mainPanel()` on the right.
- `sidebarPanel(...)`
  The sidebar area used to place various input controls (such as sliders, drop-down boxes, etc.).
- `mainPanel(...)`
  The main display area used to place output controls (such as graphics, tables, text, etc.).
- `h3(text)`
  Insert a third-level title tag, and the parameter `text` is a string.
- `br()`
  Inserts an HTML line break, equivalent to `<br>`.
- `sliderInput(inputId, label, min, max, value, ...)`
  Slider control for selecting numeric values.

  - `inputId`: The unique identifier of the control (such as `"num"`).
  - `label`: Text description above the slider.
  - `min`, `max`: value range.
  - `value`: Initial default value.
  - Other optional parameters: `step` (step size), `animate` (animation playback), etc.
- `selectInput(inputId, label, choices, selected, ...)`
  Drop down selection box.

  - `choices`: A named vector, the name is the label to be displayed to the user, and the value is the string actually returned to `input$…`.
  - `selected`: Item selected by default.
- `plotOutput(outputId, ...)`
  Reserve a drawing output area in the UI.

  - `outputId`: Corresponds to server-side `output$…`.
  - Optional parameters: `height`, `width`, etc.
- `renderPlot(expr, ...)`
  Generate graphical output on the server side.

  - `expr`: Drawing code block.
  - Optional parameters: `res` (resolution), `height`, `width`, etc.
- `rnorm(n, mean = 0, sd = 1)`
  Generate `n` random numbers that conform to the normal distribution (mean `mean`, standard deviation `sd`).
- `plot(x, y, col, pch, main, ...)`
  Basic plotting functions to draw scatter plots.

  - `col`: point color;
  - `pch`: point shape;
  - `main`: Graphic title.
- `paste(..., sep = " ", collapse = NULL)`
  The string concatenation function combines multiple values into a single string.

  - `sep`: Separator between parts.
- `shinyApp(ui, server)`
  Assemble the UI and server into a complete Shiny application and launch it.

### 2.3 Streaming layout: `fluidRow` and `column`

In this example, we use the following new functions, please first understand their basic usage and parameters:

#### Related functions and usage

- **`fluidPage(...)`**
  Create a responsive page container where all UI elements should be placed.
- **`titlePanel(title)`**
  Display a large title at the top of the page. `title` is a string.
- **`fluidRow(...)`**
  Define a "flowing" row container, which can contain several `column()` and automatically adapt to different screen widths.
- **`column(width, ...)`**
  Define a column in `fluidRow()`.

  - `width`: occupies the number of copies (1~12) in the 12-column grid system.
  - For example, `column(6, ...)` represents half the width, and `column(4, ...)` represents one-third of the width.
- **`h3(text)`**
  Insert a third-level title, `text` is a string.
- **`sliderInput(inputId, label, min, max, value, ...)`**
  Slider control:

  - `inputId`: unique identifier, used to read `input$inputId` on the server side.
  - `label`: Text description displayed above the slider.
  - `min`, `max`: value range.
  - `value`: Default value.
- **`plotOutput(outputId, ...)`**
  Reserve a drawing area in the UI. `outputId` corresponds to `output$outputId` on the server side.
- **`renderPlot(expr, ...)`**
  Execute the drawing code on the server side to generate graphical output.

  - `expr`: A block of R code, wrapped with `{ … }`.
- **`rnorm(n, mean = 0, sd = 1)`**
  Generate `n` random numbers that conform to normal distribution.
- **`hist(x, ...)`**
  Draw a histogram. `x` is a value vector.
- **`plot(x, y, type, col, main, ...)`**
  Draw a scatter plot or line chart.

  - `type = "l"` represents polyline; default is scatter point.
- **`shinyApp(ui, server)`**
  Combine the UI and server and launch the entire Shiny application.

The following example divides the first row into three columns, each with a slider; the second row is divided into two columns, each with a chart:

```r
library(shiny)

ui <- fluidPage(
  titlePanel("Flexible grid layout"),

  #First row: three parallel sliders
  fluidRow(
    column(4,  #Accounts for 4/12 width (1/3)
           h3("The first row"),
           sliderInput("slider1", "Slider 1", min = 1, max = 100, value = 50)
    ),
    column(4,  #Accounts for 4/12 width (1/3)
           h3("The second column"),
           sliderInput("slider2", "Slider 2", min = 1, max = 100, value = 50)
    ),
    column(4,  #Accounts for 4/12 width (1/3)
           h3("Third column"),
           sliderInput("slider3", "Slider 3", min = 1, max = 100, value = 50)
    )
  ),

  #Second line: Two parallel charts
  fluidRow(
    column(6,  #Accounts for 6/12 width (1/2)
           plotOutput("plot1")
    ),
    column(6,  #Accounts for 6/12 width (1/2)
           plotOutput("plot2")
    )
  )
)

server <- function(input, output) {
  output$plot1 <- renderPlot({
    hist(rnorm(input$slider1),
         col = "lightblue",
         main = paste("Histogram 1 (n =", input$slider1, ")"))
  })

  output$plot2 <- renderPlot({
    plot(1:input$slider2,
         rnorm(input$slider2),
         type = "l",
         col = "red",
         main = paste("Line chart (n =", input$slider2, ")"))
  })
}

shinyApp(ui = ui, server = server)
```

12-column system description

- The total width of each line (`fluidRow`) is divided into 12 parts
- `n` of `column(n, ...)` indicates how many copies are occupied
- For example: `column(4)` occupies one-third, `column(6)` occupies one-half, and `column(12)` occupies the entire row

## 3. Multi-tab page: tabsetPanel

Before learning about multi-tab layout, let's first understand a few new Shiny functions and concepts:

- **`tabsetPanel(...)`**
  Create a tab control container to display multiple panels (Tabs) at the same location.
- **`tabPanel(title, ...)`**
  Define a single tab page.

  - `title`: The text displayed on the tab page.
  - The following `...` part is the UI element to be displayed on this page.
- **`sidebarLayout(sidebarPanel, mainPanel)`**
  The classic sidebar layout has input controls on the left and output and content on the right.
- **`sidebarPanel(...)`** and **`mainPanel(...)`**
  Placed on the left and right sides of `sidebarLayout()` respectively, used to organize input (left) and output or other content (right).
- **`reactive({ ... })`**
  Define a reactive expression that automatically recalculates and caches the result when its internal dependency `input$…` changes.
- **Output Function**

  - `plotOutput("id")` corresponds to `renderPlot({ ... })` on the server side and is used for drawing.
  - `tableOutput("id")` corresponds to `renderTable({ ... })` on the server side and is used to display data tables.
- **UI layout function**

  - `fluidPage(...)`: Page top-level container.
  - `titlePanel("Title")`: Page title.
  - `h3("Text")`, `p("Paragraph")`: Insert a third-level heading and paragraph text, respectively.

After mastering the above components, you can use tabs to flexibly switch between different views in the same application.

### 3.1 Basic tab page

```r
library(shiny)

ui <- fluidPage(
  titlePanel("Example of multiple tabs"),

  sidebarLayout(
    sidebarPanel(
      sliderInput("n", "Number of data points:", 10, 100, 50)
    ),

    mainPanel(
      #Label page board
      tabsetPanel(
        #The first label
        tabPanel("Histogram",
                 h3("Data distribution"),
                 plotOutput("hist")
        ),

        #The second label
        tabPanel("Scatter plot",
                 h3("Data scatter plot"),
                 plotOutput("scatter")
        ),

        #The third label
        tabPanel("data",
                 h3("raw data"),
                 tableOutput("table")
        ),

        #The fourth label
        tabPanel("explain",
                 h3("About this App"),
                 p("This is an example of a demonstration of multiple tabs."),
                 p("You can switch between different labels to view different content.")
        )
      )
    )
  )
)

server <- function(input, output) {
  #Generate data (all tags shared)
  data <- reactive({
    data.frame(
      x = rnorm(input$n),
      y = rnorm(input$n)
    )
  })

  output$hist <- renderPlot({
    hist(data()$x,
         col = "lightgreen",
         main = "Distribution of the variable X")
  })

  output$scatter <- renderPlot({
    plot(data()$x, data()$y,
         col = "blue",
         pch = 19,
         main = "X vs Y")
  })

  output$table <- renderTable({
    head(data(), 10)  #Only the first 10 lines are displayed.
  })
}

shinyApp(ui = ui, server = server)
```

### 3.2 Navigation bar page: `navbarPage`

In Shiny, if you want to be able to switch between different "pages" at the top of the website, you can use **Navigation Bar Layout**. The core functions are:

- **`navbarPage(title, ...)`**
  Create an application framework with a navigation bar.

  - `title`: Application name, displayed on the far left.
- **`tabPanel(title, ...)`**
  Define a tab (page) in the navigation bar.

  - `title`: The text on the navigation bar for this page.
- **`sidebarLayout(sidebarPanel, mainPanel)`**
  Classic left-right structure: input controls on the left and output on the right.
- **`fileInput(inputId, label, ...)`**
  File upload control:

  - `inputId`: for `input$inputId` reading.
  - `label`: Displayed description text.
- **`checkboxInput(inputId, label, value = TRUE/FALSE)`**
  Single checkbox control:

  - `value`: Whether selected by default.
- **`selectInput(inputId, label, choices, ...)`**
  Drop-down selection box:

  - `choices`: optional vector or named vector.
- **`tableOutput(outputId)`** and **`renderTable({ ... })`**
  Reserve the table area in the UI and generate it in the server.
- **`plotOutput(outputId)`** and **`renderPlot({ ... })`**
  Reserve a drawing area in the UI and generate graphics in the server.

---

**Full sample code (with full comments)**

```r
library(shiny)

#UI part
ui <- navbarPage(
  title = "My data analysis platform",  #The app name is displayed on the far left of the navigation bar.

  #---- First page: Data import ----
  tabPanel("Data import",
    sidebarLayout(
      #Left: File Upload and Options
      sidebarPanel(
        #Upload CSV file
        fileInput(
          inputId = "file",
          label   = "Select the CSV file:"
        ),
        br(),  #Line spacing

        #Whether the header is included
        checkboxInput(
          inputId = "header",
          label   = "The file contains a header.",
          value   = TRUE
        )
      ),

      #Right: Shows the uploaded content
      mainPanel(
        tableOutput("contents")
      )
    )
  ),

  #---- Second page: Data visualization ----
  tabPanel("Data visualization",
    sidebarLayout(
      #Left: Chart type selection
      sidebarPanel(
        selectInput(
          inputId = "plotType",
          label   = "Select the chart type:",
          choices = c("Histogram", "Box diagram", "Scatter plot"),
          selected = "Histogram"
        )
      ),

      #Right side: Draw according to the selection.
      mainPanel(
        plotOutput("plot")
      )
    )
  ),

  #---- Third page: About ----
  tabPanel("about",
    h2("About this application"),
    p("Version: 1.0"),
    p("Author: Your name"),
    p("This is a data analysis demonstration application.")
  )
)

#Server part
server <- function(input, output) {

  #Render the table: Use static data during the demonstration, which can be replaced by read.csv(input$file$datapath, header = input$header) in practice.
  output$contents <- renderTable({
    #Simplified example: Return two columns of data
    data.frame(
      Column1 = 1:5,
      Column2 = letters[1:5]
    )
  })

  #Render charts: Choose to draw different graphics according to the dropdown box.
  output$plot <- renderPlot({
    if (input$plotType == "Histogram") {
      #Draw a histogram
      hist(
        rnorm(100),               #Random data
        col  = "lightblue",       #Fill color
        main = "Histogram example"
      )

    } else if (input$plotType == "Box diagram") {
      #Draw a box line diagram
      boxplot(
        rnorm(100),
        col  = "lightgreen",
        main = "Box line icon example"
      )

    } else {
      #Draw a scatter plot
      plot(
        rnorm(100), rnorm(100),   #Two sets of random data
        pch  = 19,                #The shape of the dot
        col  = "red",             #The color of the dots
        main = "Example of scatter plot"
      )
    }
  })
}

#Launch the Shiny app
shinyApp(ui = ui, server = server)
```

## 4. Add HTML elements to beautify

### 4.1 Commonly used HTML tags

```r
library(shiny)

ui <- fluidPage(
  #Various text formats
  h1("Level 1 title - maximum"),
  h2("Secondary title"),
  h3("Level 3 title"),
  h4("Level 4 title"),

  p("This is an ordinary paragraph."),

  p("This paragraph has", strong("Bold text"), "and", em("Italic text"), "。"),

  #Separator line
  hr(),

  #Colored text
  p(style = "color:red;", "This is red text."),
  p(style = "color:blue; font-size:20px;", "This is blue large text."),

  #List
  tags$ul(
    tags$li("List item 1"),
    tags$li("List item 2"),
    tags$li("List item 3")
  ),

  #Link
  tags$a(href = "https://shiny.posit.co/", "Visit the official website of Shiny"),

  br(),
  br(),

  #Pictures (if any)
  # tags$img(src = "logo.png", height = 100)
)

server <- function(input, output) {
}

shinyApp(ui = ui, server = server)
```

### 4.2 Use wellPanel to create panels

```r
library(shiny)

ui <- fluidPage(
  titlePanel("Use the content of the skin tissue."),

  fluidRow(
    column(6,
           wellPanel(
             h4("control panel"),
             sliderInput("n1", "Parameter 1:", 1, 100, 50),
             sliderInput("n2", "Parameter 2:", 1, 100, 30),
             p("These controls are in a gray panel.")
           )
    ),

    column(6,
           wellPanel(
             h4("Information panel"),
             p("Current time:", Sys.time()),
             p("R version:", R.version.string),
             tags$ul(
               tags$li("It looks more tidy like this."),
               tags$li("The content is organized together."),
               tags$li("Visually clearer")
             )
           )
    )
  )
)

server <- function(input, output) {
}

shinyApp(ui = ui, server = server)
```

## 5. Use themes to beautify: shinythemes

### 5.1 Install and use themes

#### Prerequisite knowledge

- **`shinythemes` Package**
  Provides a variety of Bootstrap themes to quickly skin your Shiny application.
- **`theme = shinytheme("…")`**
  Specify the theme at startup through the `theme` parameter in `fluidPage()`.
- **`themeSelector()`**
  Built-in theme preview drop-down menu allows switching themes instantly at runtime.
- **Button style class (`class`)**

  - `btn-primary`: Indicates the "Main" button (blue background).
  - `btn-warning`: Indicates the "Warning" button (orange background).
  - These classes are from Bootstrap and can be passed to functions such as `actionButton()` through the `class` parameter.

---

#### Complete sample code

```r
library(shiny)
library(shinythemes)

ui <- fluidPage(
  theme = shinytheme("cerulean"),  #Default theme
  themeSelector(),                 #The theme can be switched at runtime.

  titlePanel("Use the Shiny App with the theme"),

  sidebarLayout(
    sidebarPanel(
      h3("control panel"),

      sliderInput(
        inputId = "num",
        label   = "Number of data points:",
        min     = 50,
        max     = 200,
        value   = 100
      ),

      #Primary Buttons: Blue Background
      actionButton(
        inputId = "action",
        label   = "Click on me.",
        class   = "btn-primary"
      ),

      br(), br(),  #Two line breaks

      #Warning button: orange background
      actionButton(
        inputId = "action2",
        label   = "Secondary operation",
        class   = "btn-warning"
      )
    ),

    mainPanel(
      tabsetPanel(
        tabPanel("chart",
                 plotOutput("plot")
        ),
        tabPanel("data",
                 tableOutput("table")
        ),
        tabPanel("explain",
                 h3("Different theme appearances"),
                 p("After switching themes, you will see:"),
                 tags$ul(
                   tags$li("Color scheme changes"),
                   tags$li("Font and spacing changes"),
                   tags$li("Button style changes"),
                   tags$li("Overall visual effect difference")
                 )
        )
      )
    )
  )
)

server <- function(input, output, session) {
  #Responsive data
  data <- reactive({
    data.frame(
      x = rnorm(input$num),
      y = rnorm(input$num)
    )
  })

  #Render scatter plots
  output$plot <- renderPlot({
    plot(
      data()$x, data()$y,
      col  = "darkblue",
      pch  = 19,
      main = "Random scatter plot"
    )
  })

  #Render the form
  output$table <- renderTable({
    head(iris, 10)
  })
}

shinyApp(ui = ui, server = server)
```

### 5.2 Comparison of theme effects

Features of different themes:

- **cerulean**: blue tone, professional feel
- **cosmo**: Flat design, modern feel
- **flatly**: minimalist style, refreshing
- **journal**: journalistic style, formal
- **readable**: Pay attention to readability
- **spacelab**: sense of technology
- **united**: orange tone, vitality
- **yeti**: blue-gray tone, calm

## 6. Comprehensive exercise: Building a clearly structured app

In this section, we will complete a small exercise of "Personal Information Management System" step by step, through the following steps:

1. **Build the item skeleton**
2. **Add input control**
3. **Render personal information card based on submit button**
4. **Draw age distribution statistics**
5. **Beautify the layout and theme**

---

### 6.1 Build item skeleton

First, create a minimalist `app.R`, load the necessary packages and define empty `ui` and `server`:

```r
library(shiny)
library(shinythemes)

ui <- fluidPage(
  #Leave it empty here first.
)

server <- function(input, output, session) {
  #Leave it empty here first.
}

shinyApp(ui, server)
```

Save and run to confirm that a blank Shiny application can be started normally.

---

### 6.2 Add input controls

In `ui`, we divide the left and right columns into two columns: the "Input Information Panel" on the left and the "Output Area" on the right.

```r
ui <- fluidPage(
  theme = shinytheme("flatly"),  #Set the overall theme

  titlePanel("Personal information management system"),

  fluidRow(
    #Left side: 4/12 width, for input controls
    column(4,
      wellPanel(
        h3("Enter information"),
        textInput("name",   "Name:",    value = ""),
        numericInput("age", "Age:",    value = 25, min = 1, max = 100),
        selectInput("gender", "Gender:",
                    choices = c("man", "woman", "other")),
        selectInput("hobby",  "Hobbies:",
                    choices = c("sport", "read", "music", "tour", "delicious food")),
        actionButton("submit", "submit",
                     class = "btn-success btn-block")
      )
    ),

    #Right: 8/12 width, for Tab output
    column(8,
      tabsetPanel(
        tabPanel("Information card", br(), uiOutput("card")),
        tabPanel("count",      br(), plotOutput("stats"))
      )
    )
  )
)
```

- `wellPanel()` is used to add a background frame to the input area.
- `actionButton(..., class = "btn-success btn-block")` specifies the "Success Green" and "Full Width" styles.

---

### 6.3 Render personal information card

In `server`, monitor the submission event of `input$submit` and use `renderUI()` to dynamically generate information cards:

```r
server <- function(input, output, session) {
  output$card <- renderUI({
    #If the name has not been entered, prompt the user to fill it in first.
    if (input$name == "") {
      wellPanel(
        h4("Please enter the information on the left side."),
        p('After filling in, click the "Submit" button.')
      )
    } else {
      #Show details after entering
      wellPanel(
        h3("Personal information card"),
        hr(),
        p(strong("Name:"), input$name),
        p(strong("Age:"), paste0(input$age, "year")),
        p(strong("Gender:"), input$gender),
        p(strong("Hobbies:"), input$hobby),
        br(),
        p(em("Information submission time:"), Sys.time())
      )
    }
  })
}
```

- `uiOutput("card")`, used in conjunction with `renderUI({...})`, can insert any HTML element into the UI.

---

### 6.4 Draw age distribution statistics chart

Previously, we have reserved a `plotOutput("stats")` in the UI for the "Statistics" tab. Now we have to fill it with `renderPlot()` on the server side, as follows:

1. **Prepare data**

   - The age entered by the user is a fixed value `input$age`.
   - In order to make the graph more "contrastive", we generate another 50 random age samples: `sample(20:60, 50, replace = TRUE)`.
   - Finally merge the two parts into one vector `ages`.
2. **Draw a histogram**

```text
   hist(ages,
         col = "skyblue", # Fill color of the column
         main = "Age Distribution", # Chart title
         xlab = "Age", # x-axis label
         ylab = "number of people" # y-axis label
   )
```

3. `hist()` will automatically divide `ages` into boxes according to intervals, and count the frequency of each box.
4. **Indicate user’s age**
5. Call `abline(v = input$age, col = "red", lwd = 2)`:

   - `v = input$age` means draw a vertical line at that position on the x-axis.
   - `col = "red"` Set color to red and highlight.
   - `lwd = 2` Set the width of the line to make it more visible.
6. **Add text description**

```r
   #First, use hist(..., plot = FALSE)$counts to get the frequency of each box.
   counts <- hist(ages, plot = FALSE)$counts
   ymax   <- max(counts) * 0.8    #Take 80% of the highest frequency number as the text y coordinate.

   text(input$age,       #x coordinate: user age
         ymax,           #y coordinate: the position we calculated
         labels = "You are here.", #Text to display
         col    = "red",    #Text color
         pos    = 4         #Text placement direction: 4 = text is on the right side of the coordinate point.
   )
```

   - `hist(..., plot = FALSE)`: First perform a histogram calculation without drawing to obtain the original frequency.
   - `text(x, y, labels, col, pos)`: Draw text at the specified coordinates `(x, y)`.
   - `pos = 4` means the text is placed to the right of the point.

---

Put the above logic into the `server` function. The complete example is as follows:

```r
server <- function(input, output, session) {
  #... The renderUI of the personal information card is above...

  output$stats <- renderPlot({
    #1. Prepare data
    ages <- c(input$age,
              sample(20:60, 50, replace = TRUE))

    #2. Draw a histogram
    hist(ages,
         col   = "skyblue",
         main  = "Age distribution",
         xlab  = "age",
         ylab  = "number of people")

    #3. Mark the user's age.
    abline(v = input$age, col = "red", lwd = 2)

    #4. Calculate the appropriate position of the text and add the text.
    counts <- hist(ages, plot = FALSE)$counts
    ymax   <- max(counts) * 0.8
    text(input$age, ymax,
         labels = "You are here.",
         col    = "red",
         pos    = 4)
  })
}
```

In this way, when the user switches to the "Statistics" tab and clicks the "Submit" button, he or she will see a histogram containing the user's age tag.

---

### 6.5 Complete code

Integrate the above parts to get the final runnable `app.R`:

```r
library(shiny)
library(shinythemes)

ui <- fluidPage(
  theme = shinytheme("flatly"),

  titlePanel("Personal information management system"),

  fluidRow(
    column(4,
      wellPanel(
        h3("Enter information"),
        textInput("name",   "Name:",    value = ""),
        numericInput("age", "Age:",    value = 25, min = 1, max = 100),
        selectInput("gender", "Gender:",
                    choices = c("man", "woman", "other")),
        selectInput("hobby",  "Hobbies:",
                    choices = c("sport", "read", "music", "tour", "delicious food")),
        actionButton("submit", "submit",
                     class = "btn-success btn-block")
      )
    ),
    column(8,
      tabsetPanel(
        tabPanel("Information card", br(), uiOutput("card")),
        tabPanel("count",      br(), plotOutput("stats"))
      )
    )
  )
)

server <- function(input, output, session) {
  output$card <- renderUI({
    if (input$name == "") {
      wellPanel(
        h4("Please enter the information on the left side."),
        p('After filling in, click the "Submit" button.')
      )
    } else {
      wellPanel(
        h3("Personal information card"),
        hr(),
        p(strong("Name:"), input$name),
        p(strong("Age:"), paste0(input$age, "year")),
        p(strong("Gender:"), input$gender),
        p(strong("Hobbies:"), input$hobby),
        br(),
        p(em("Information submission time:"), Sys.time())
      )
    }
  })

  output$stats <- renderPlot({
    ages <- c(input$age, sample(20:60, 50, replace = TRUE))
    hist(ages,
         col   = "skyblue",
         main  = "Age distribution",
         xlab  = "age",
         ylab  = "number of people")
    abline(v = input$age, col = "red", lwd = 2)
    text(input$age,
         max(hist(ages, plot = FALSE)$counts) * 0.8,
         labels = "You are here.", col = "red", pos = 4)
  })
}

shinyApp(ui = ui, server = server)
```

After completion, run `shinyApp(ui, server)` to experience an interactive and clearly structured personal information management small application.

## 7. Today’s summary

### 7.1 Summary of layout methods

1. **Basic layout:**

   - `fluidPage()` - Responsive page container
   - `titlePanel()` - Add title
2. **Commonly used layouts:**

   - `sidebarLayout()` - Sidebar layout (most commonly used)
   - `fluidRow()` + `column()` - Grid layout (flexible)
   - `wellPanel()` - Content Panel (Organize Content)
3. **Multiple Pages:**

   - `tabsetPanel()` + `tabPanel()` - Tab page
   - `navbarPage()` - Navigation bar page

### 7.2 Summary of beautification methods

1. **HTML tag:**

   - Title: `h1()` to `h6()`
   - Text: `p()`, `strong()`, `em()`
   - Others: `hr()`, `br()`, `tags$ul()`
2. **Style:**

   - Inline style: `style = "color:red;"`
   - Button type: `class = "btn-primary"`
3. **Topic:**

   - using `shinythemes` package
   - `theme = shinytheme("theme_name")`

### 7.3 Important reminder

Common mistakes

1. Forgot to load the `shinythemes` package
2. The sum of column widths exceeds 12
3. Nesting level confusion (prioritize checking indentation and bracket matching)
4. Wrong comma position (no comma in the last element)

you learned

- Use professional layouts to keep your app organized
- Organize complex content with tabs
- Add HTML elements to enrich the interface
- Switch themes and change appearance with one click

Tomorrow we'll learn more about input controls that let users interact with your app in a variety of ways!
