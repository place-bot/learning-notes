# Day 3: Various input controls - let users interact with your app

## 1. Before you begin: Understanding input controls

### 1.1 What is an input control?

Input controls are things on a web page that users can click, input, and select. For example:

- Button - user clicks
- Text box - user enters text
- Drop down box - user selects options
- Slider - user drags to select a value

### 1.2 General rules for input controls

All input controls have two required parameters:

1. **inputId** - Give the control a name (ID card)
2. **label** - Description text displayed to the user

Let's start with the simplest!

## 2. Text input box: textInput()

### 2.1 The most basic text input

Let's first create the simplest text input box:

```r
library(shiny)

ui <- fluidPage(
  #Create a text input box
  textInput("name", "Please enter your name:")
)

server <- function(input, output) {
  #Do nothing for the time being.
}

shinyApp(ui = ui, server = server)
```

After running, you will see an input box, but nothing will happen after entering the content.

### 2.2 Display the input content

Now let's display what the user entered:

```r
library(shiny)

ui <- fluidPage(
  textInput("name", "Please enter your name:"),

  #Add a place to display text.
  textOutput("greeting")
)

server <- function(input, output) {
  #Now we need to deal with the input.
  output$greeting <- renderText({
    input$name  #Get the content entered by the user
  })
}

shinyApp(ui = ui, server = server)
```

Try typing your name and it will appear instantly!

### 2.3 Make the output more friendly

We can process the output content:

```r
library(shiny)

ui <- fluidPage(
  textInput("name", "Please enter your name:"),
  textOutput("greeting")
)

server <- function(input, output) {
  output$greeting <- renderText({
    #If not entered, a prompt will appear.
    if(input$name == "") {
      "Please enter your name above."
    } else {
      #If entered, greeting message is displayed.
      paste("Hello,", input$name, "!Welcome to use Shiny!")
    }
  })
}

shinyApp(ui = ui, server = server)
```

### 2.4 More options for textInput

#### Detailed explanation of `verbatimTextOutput()` usage

In Shiny's UI, `verbatimTextOutput(outputId)` is used to create a "verbatim output" area (monoswidth font), which can fully retain spaces, line breaks, and console-style formatting, suitable for display:

- Print result of R object (such as `summary()`, `str()`, etc.)
- Debug information or logs
- Any text that needs to retain its original formatting

It is usually used with `renderPrint({ ... })` on the server side:

- **UI terminal**

```text
  verbatimTextOutput("allText")
```

- **Server side**

```r
  output$allText <- renderPrint({
      #Write the R code that needs to be "printed" here.
      summary(some_data)
  })
```

---

Here's a complete example that demonstrates four different uses of `textInput()` and summarizes all inputs into a `verbatimTextOutput` region.

#### Code Example

```r
library(shiny)

ui <- fluidPage(
  h3("Various uses of textInput"),

  #1. Basic usage
  textInput("text1", "Basic input box:"),

  #2. With default value
  textInput("text2", "With default value:", value = "I am the default text."),

  #3. With placeholders (prompt text)
  textInput("text3", "With prompt text:", placeholder = "Please enter the email address."),

  #4. Width restriction
  textInput("text4", "A narrower input box:", width = "200px"),

  hr(),

  h4("What you entered:"),
  #Create a uniform width text output area to display the results of the server-side renderPrint.
  verbatimTextOutput("allText")
)

server <- function(input, output) {
  #Concatenate the values of all four input boxes and "print" them to the verbatimTextOutput area.
  output$allText <- renderPrint({
    paste(
      "Input box 1:", input$text1, "\n",
      "Input box 2:", input$text2, "\n",
      "Input box 3:", input$text3, "\n",
      "Input box 4:", input$text4
    )
  })
}

shinyApp(ui = ui, server = server)
```

## 3. Numeric input box: numericInput()

### 3.1 Basic digital input

When we need the user to enter a number, use `numericInput()`:

```r
library(shiny)

ui <- fluidPage(
  #Create a digital input box
  numericInput("age", "Please enter your age:", value = 18)
)

server <- function(input, output) {
}

shinyApp(ui = ui, server = server)
```

Note: This input box can only enter numbers!

### 3.2 Set the number range

We can limit the range of input:

```r
library(shiny)

ui <- fluidPage(
  numericInput("age",
               "Please enter your age:",
               value = 18,      #Default value
               min = 0,         #Minimum value
               max = 150,       #Maximum value
               step = 1)        #Step length (how much does it increase or decrease when you click the arrow)
)

server <- function(input, output) {
}

shinyApp(ui = ui, server = server)
```

### 3.3 Use numerical input to perform calculations

Let’s make a BMI calculator:

```r
library(shiny)

ui <- fluidPage(
  h3("BMI calculator"),

  #Step 1: Add height input
  numericInput("height", "Height (cm):",
               value = 170, min = 50, max = 250),

  #Step 2: Add weight input
  numericInput("weight", "Weight (kg):",
               value = 60, min = 20, max = 200),

  #Step 3: Where the results are displayed
  h4("Your BMI is:"),
  textOutput("bmi"),
  textOutput("status")
)

server <- function(input, output) {
  #Calculate BMI
  output$bmi <- renderText({
    #BMI = weight (kg) / (height (m))^2
    height_m <- input$height / 100  #centimeters to meters
    bmi_value <- input$weight / (height_m ^ 2)
    round(bmi_value, 1)  #Keep one decimal place.
  })

  #Display health status
  output$status <- renderText({
    height_m <- input$height / 100
    bmi_value <- input$weight / (height_m ^ 2)

    if(bmi_value < 18.5) {
      "Slightly underweight"
    } else if(bmi_value < 24) {
      "Normal weight"
    } else if(bmi_value < 28) {
      "overweight"
    } else {
      "Need to lose weight"
    }
  })
}

shinyApp(ui = ui, server = server)
```

## 4. Slider input: sliderInput()

### 4.1 Basic slider

Sliders are an intuitive way to select numbers:

```r
library(shiny)

ui <- fluidPage(
  h3("Slider demonstration"),

  #Basic slider
  sliderInput("slider1", "Choose a number:",
              min = 0,
              max = 100,
              value = 50),

  #Display the selected value
  textOutput("value1")
)

server <- function(input, output) {
  output$value1 <- renderText({
    paste("You have chosen:", input$slider1)
  })
}

shinyApp(ui = ui, server = server)
```

### 4.2 Various forms of slider

There are many ways to use sliders, let’s try them one by one:

```r
library(shiny)

ui <- fluidPage(
  h3("Various forms of sliders"),

  #1. Basic slider
  sliderInput("basic", "Basic slider:",
              min = 0, max = 100, value = 50),

  #2. Slider with step length
  sliderInput("step", "Move 5 each time (step length = 5):",
              min = 0, max = 100, value = 50,
              step = 5),

  #3. Range slider (select the interval)
  sliderInput("range", "Selection range:",
              min = 0, max = 100,
              value = c(25, 75)),  #Note: There are two values here!

  #4. Sliders with animation
  sliderInput("animate", "Can be played automatically:",
              min = 1, max = 10, value = 1,
              animate = TRUE),  #Add a play button

  hr(),
  verbatimTextOutput("allValues")
)

server <- function(input, output) {
  output$allValues <- renderPrint({
    paste("Basic slider:", input$basic, "\n",
          "Step length slider:", input$step, "\n",
          "Range slider:", input$range[1], "-", input$range[2], "\n",
          "Animation slider:", input$animate)
  })
}

shinyApp(ui = ui, server = server)
```

### 4.3 Use slider to control graphics

This is the most common usage:

```r
library(shiny)

ui <- fluidPage(
  titlePanel("Slider control graphics"),

  sidebarLayout(
    sidebarPanel(
      #Control the number of data points
      sliderInput("n_points", "Number of data points:",
                  min = 10, max = 500, value = 100),

      #The size of the control point
      sliderInput("point_size", "The size of the dot:",
                  min = 0.5, max = 5, value = 2,
                  step = 0.5),

      #Control transparency
      sliderInput("alpha", "Transparency:",
                  min = 0.1, max = 1, value = 0.7,
                  step = 0.1)
    ),

    mainPanel(
      plotOutput("scatter")
    )
  )
)

server <- function(input, output) {
  output$scatter <- renderPlot({
    #Generate random data
    x <- rnorm(input$n_points)
    y <- rnorm(input$n_points)

    #Draw a scatter plot
    plot(x, y,
         pch = 19,  #Solid round dot
         cex = input$point_size,  #The size of the dot
         col = rgb(0, 0, 1, input$alpha),  #Blue, variable transparency
         main = paste(input$n_points, "A data point"))
  })
}

shinyApp(ui = ui, server = server)
```

## 5. Drop-down selection box: selectInput()

### 5.1 Basic drop-down box

When the user needs to choose from several options:

```r
library(shiny)

ui <- fluidPage(
  h3("Dropdown box demonstration"),

  #Create a dropdown
  selectInput("fruit", "Choose your favorite fruit:",
              choices = c("Apple", "banana", "orange", "grape")),

  textOutput("selected")
)

server <- function(input, output) {
  output$selected <- renderText({
    paste("You have chosen:", input$fruit)
  })
}

shinyApp(ui = ui, server = server)
```

### 5.2 Set option values

Sometimes the text displayed to the user is different from the actual value used:

```r
library(shiny)

ui <- fluidPage(
  h3("The displayed value and the actual value of the option"),

  #Method 1: Display the same value as the value.
  selectInput("simple", "Simple options:",
              choices = c("red", "blue", "green")),

  #Method 2: The display value is different from the value.
  selectInput("advanced", "Advanced options:",
              choices = c("red" = "red",
                          "blue" = "blue",
                          "green" = "green")),

  verbatimTextOutput("values")
)

server <- function(input, output) {
  output$values <- renderPrint({
    paste("Value of simple options:", input$simple, "\n",
          "Value of advanced options:", input$advanced)
  })
}

shinyApp(ui = ui, server = server)
```

### 5.3 Multi-select drop-down box

Allow users to select multiple options:

```r
library(shiny)

ui <- fluidPage(
  h3("Multi-select dropdown box"),

  selectInput("skills", "Choose the programming language you know:",
              choices = c("R", "Python", "JavaScript",
                          "Java", "C++", "SQL"),
              multiple = TRUE),  #Many choices are allowed!

  textOutput("selected")
)

server <- function(input, output) {
  output$selected <- renderText({
    if(length(input$skills) == 0) {
      "You haven't made a choice yet."
    } else {
      paste("You will:", paste(input$skills, collapse = ", "))
    }
  })
}

shinyApp(ui = ui, server = server)
```

## 6. Radio buttons: radioButtons()

### 6.1 Basic radio buttons

When there are not many options and you want to display them all:

```r
library(shiny)

ui <- fluidPage(
  h3("Single-choice button"),

  radioButtons("gender", "Choose gender:",
               choices = c("man", "woman", "other")),

  textOutput("selected")
)

server <- function(input, output) {
  output$selected <- renderText({
    paste("You have chosen:", input$gender)
  })
}

shinyApp(ui = ui, server = server)
```

### 6.2 Horizontal arrangement and setting default values

```r
library(shiny)

ui <- fluidPage(
  h3("More options for the single-select button"),

  #Vertical alignment (default)
  radioButtons("size1", "Clothing size (vertical):",
               choices = c("S", "M", "L", "XL"),
               selected = "M"),  #Default select M

  #Horizontal arrangement
  radioButtons("size2", "Clothing size (horizontal):",
               choices = c("S", "M", "L", "XL"),
               selected = "M",
               inline = TRUE),  #Arranged horizontally!

  verbatimTextOutput("sizes")
)

server <- function(input, output) {
  output$sizes <- renderPrint({
    paste("Vertical selection:", input$size1, "\n",
          "Horizontal selection:", input$size2)
  })
}

shinyApp(ui = ui, server = server)
```

## 7. Checkbox: checkboxInput() and checkboxGroupInput()

### 7.1 Single checkbox

For yes/no selection:

```r
library(shiny)

ui <- fluidPage(
  h3("Single checkbox"),

  checkboxInput("agree", "I agree to the user agreement."),

  #Displays different content based on whether checked or not
  uiOutput("nextStep")
)

server <- function(input, output) {
  output$nextStep <- renderUI({
    if(input$agree) {
      actionButton("continue", "continue", class = "btn-success")
    } else {
      p("Please agree to the user agreement first.", style = "color:red;")
    }
  })
}

shinyApp(ui = ui, server = server)
```

### 7.2 Checkbox group

Multiple options can be selected at the same time:

```r
library(shiny)

ui <- fluidPage(
  h3("Checkbox group"),

  checkboxGroupInput("hobbies", "Choose your hobbies (multiple choices are allowed):",
                     choices = c("sport", "read", "music",
                                 "tour", "delicious food", "film")),

  textOutput("selected")
)

server <- function(input, output) {
  output$selected <- renderText({
    if(length(input$hobbies) == 0) {
      "You haven't chosen any hobbies yet."
    } else {
      paste("Your hobbies include:",
            paste(input$hobbies, collapse = "、"))
    }
  })
}

shinyApp(ui = ui, server = server)
```

## 8. Date input: dateInput() and dateRangeInput()

### 8.1 Single date selection

```r
library(shiny)

ui <- fluidPage(
  h3("Date selector"),

  dateInput("birthday", "Choose your birthday:",
            value = "2000-01-01",  #Default value
            format = "yyyy-mm-dd",  #Date format
            language = "zh-CN"),    #Chinese interface

  textOutput("age")
)

server <- function(input, output) {
  output$age <- renderText({
    #Calculate age
    today <- Sys.Date()
    age <- as.numeric(today - input$birthday) / 365.25
    paste("You are about", round(age, 1), "year")
  })
}

shinyApp(ui = ui, server = server)
```

### 8.2 Date range selection

```r
library(shiny)

ui <- fluidPage(
  h3("Select date range"),

  dateRangeInput("dateRange", "Select the start and end dates:",
                 start = Sys.Date() - 30,  #Default start: 30 days ago
                 end = Sys.Date(),         #Default end: today
                 language = "zh-CN"),

  textOutput("days")
)

server <- function(input, output) {
  output$days <- renderText({
    #Calculate the number of days
    days <- as.numeric(input$dateRange[2] - input$dateRange[1])
    paste("You have chosen.", days + 1, "The data of the sky")
  })
}

shinyApp(ui = ui, server = server)
```

## 9. File upload: fileInput()

### 9.1 Basic file upload

```r
library(shiny)

ui <- fluidPage(
  h3("File upload"),

  fileInput("file", "Select a file:",
            accept = c(".csv", ".txt")),  #Restrict file types

  tableOutput("contents")
)

server <- function(input, output) {
  output$contents <- renderTable({
    #Check for any uploaded files
    if(is.null(input$file)) {
      return(NULL)
    }

    #Read CSV files
    read.csv(input$file$datapath)
  })
}

shinyApp(ui = ui, server = server)
```

### 9.2 Display file information

```r
library(shiny)

ui <- fluidPage(
  h3("File upload details"),

  fileInput("file", "Select any file:"),

  h4("File information:"),
  verbatimTextOutput("fileInfo"),

  h4("Preview of the document content:"),
  verbatimTextOutput("preview")
)

server <- function(input, output) {
  output$fileInfo <- renderPrint({
    if(is.null(input$file)) {
      "No files have been uploaded yet."
    } else {
      paste("File name:", input$file$name, "\n",
            "File size:", input$file$size, "Byte \n",
            "File type:", input$file$type)
    }
  })

  output$preview <- renderPrint({
    if(is.null(input$file)) {
      return(NULL)
    }

    #Displays different content based on the document type
    if(grepl("\\.csv$", input$file$name)) {
      head(read.csv(input$file$datapath), 5)
    } else if(grepl("\\.txt$", input$file$name)) {
      readLines(input$file$datapath, n = 5)
    } else {
      "This file type is not supported for preview."
    }
  })
}

shinyApp(ui = ui, server = server)
```

## 10 Comprehensive exercise: build iris data filter step by step

Goal: Allow users to filter the `iris` data set, select displayed columns, varieties, calyx length range, number of rows, and finally download the results.

---

### Step 1: Preparation

```r
#Load the Shiny package
library(shiny)
```

---

### Step 2: Build the user interface (UI)

In a Shiny app, the UI is the part of the interface that users see and operate on. We will use `fluidPage()` to define a responsive layout and use `sidebarLayout()` to divide the input control area on the left and the output display area on the right.

We will not directly write the entire UI to death, but build each component in a modular and step-by-step manner, and finally combine it into a complete UI.

---

#### 🎯 Goal: Build an interactive data filtering panel, including 5 functional controls:

|No.|Control type|Function description|
| --- | --- | --- |
| 1 |checkbox group|User selects which variable columns to display|
| 2 |drop down menu|User selects a certain variety or all data|
| 3 |Slider|Filter range to limit calyx length|
| 4 |Numeric input box|Control the first few rows of displayed data|
| 5 |download button|Download filtered data as CSV file|

---

#### 🧩 Submodule 1: Select the columns to display `checkboxGroupInput()`

##### ✅ Design ideas:

Users may not need to view all variables. We use check boxes to list all column names of iris to allow users to check the fields they are interested in.

##### ✅ Code example:

```text
checkboxGroupInput(
  inputId = "columns", # The unique ID of the control
  label = "Select the columns to be displayed:", # The prompt text displayed above the control
  choices = names(iris), # Optional: all column names of the iris data set
  selected = names(iris) # All checked by default
)
```

---

#### 🧩 Sub-module 2: Select variety `selectInput()`

##### ✅ Design ideas:

There are three categories of plant species in the iris dataset. We allow users to select a category or select "all".

##### ✅ Code example:

```text
selectInput(
  inputId = "species",
  label = "Select a variety:",
  choices = c("all", unique(iris$Species)), # Add "all" option
  selected = "all" # Display all varieties by default
)
```

---

#### 🧩 Sub-module 3: Calyx length range screening `sliderInput()`

##### ✅ Design ideas:

Use the slider to allow the user to select a filter interval for calyx length. The slider supports double-ended dragging to indicate the range.

##### ✅ Code example:

```text
sliderInput(
  inputId = "sepalLength",
  label = "Calyx length range:",
  min = min(iris$Sepal.Length), # Left border
  max = max(iris$Sepal.Length), #right boundary
  value = c(min(iris$Sepal.Length), max(iris$Sepal.Length)), # Initial range
  step = 0.1 #The interval between each move
)
```

---

#### 🧩 Sub-module 4: Control the number of display lines `numericInput()`

##### ✅ Design ideas:

Sometimes you only want to see part of the data, so you allow the user to specify the "first few rows" of data.

##### ✅ Code example:

```text
numericInput(
  inputId = "rows",
  label = "Show the first few lines:",
  value = 10, # Display 10 lines by default
  min = 1, max = 150
)
```

---

#### 🧩 Sub-module 5: Download filter result `downloadButton()`

##### ✅ Design ideas:

Allows users to export the currently filtered results to a CSV file for easy saving and sharing.

##### ✅ Code example:

```text
downloadButton(
  outputId = "download", #corresponds to the downloadHandler in the server
  label = "Download filter result"
)
```

---

#### 🧩 Combination: Put all controls into `sidebarPanel()`

```text
sidebarPanel(
  h4("Filter conditions"),

  # Control 1: Column selection
  checkboxGroupInput("columns", "Select columns to display:",
                     choices = names(iris),
                     selected = names(iris)),

  hr(), # dividing line

  # Control 2: Variety selection
  selectInput("species", "Select species:",
              choices = c("all", unique(iris$Species)),
              selected = "all"),

  # Control 3: Calyx length range
  sliderInput("sepalLength", "Calyx length range:",
              min = min(iris$Sepal.Length),
              max = max(iris$Sepal.Length),
              value = c(min(iris$Sepal.Length), max(iris$Sepal.Length)),
              step = 0.1),

  # Control 4: Display the number of rows
  numericInput("rows", "Display the first few rows:",
               value = 10, min = 1, max = 150),

  hr(),

  # Control 5: Download button
  downloadButton("download", "Download filter result")
)
```

---

#### 📤 Main panel `mainPanel()`: display result

```text
mainPanel(
  h4("filter result"),
  tableOutput("table"),

  hr(),

  h4("Data Summary"),
  verbatimTextOutput("summary")
)
```

---

#### 🧱 Complete UI build

Now we merge the sidebar and main panel into `fluidPage()` to form a complete `ui`:

```r
ui <- fluidPage(
  titlePanel("Iris data filter"),   #Application title

  sidebarLayout(
    sidebarPanel(
      h4("Screening conditions"),
      checkboxGroupInput("columns", "Select the columns to display:",
                         choices = names(iris),
                         selected = names(iris)),
      hr(),
      selectInput("species", "Choose the variety:",
                  choices = c("total", unique(iris$Species)),
                  selected = "total"),
      sliderInput("sepalLength", "Range of calyx length:",
                  min = min(iris$Sepal.Length),
                  max = max(iris$Sepal.Length),
                  value = c(min(iris$Sepal.Length), max(iris$Sepal.Length)),
                  step = 0.1),
      numericInput("rows", "Display the first few lines:",
                   value = 10, min = 1, max = 150),
      hr(),
      downloadButton("download", "Download the filtered results")
    ),

    mainPanel(
      h4("Screening results"),
      tableOutput("table"),
      hr(),
      h4("Data summary"),
      verbatimTextOutput("summary")
    )
  )
)
```

---

#### ✅ Tips

- The `inputId` value of all controls must be unique;
- `outputId` in the output part will be matched with `output$xxx <- renderXXX()` in `server`;
- If you want to beautify the interface, you can use advanced functions such as `theme`, `tags$style`, or `bslib`.

---

### Step 3: Build server logic `server`

We use `server <- function(input, output) { ... }` to define **all calculation and response behaviors**. All reading of UI controls comes from `input$xxx`, and all output is done through `output$xxx <- renderXXX(...)`.

---

### 🧩 Module 1: Data filtering logic `filteredData`

---

#### 🎯 Goal

Based on user selection:

- Variety (`input$species`)
- Calyx length range (`input$sepalLength`)
- Displayed column (`input$columns`)
- Number of rows displayed (`input$rows`)

Dynamically generate filtered `iris` data.

---

#### 🧠 Explanation of ideas

`reactive({...})` in Shiny is a reactive function container that recalculates whenever the relevant input changes.

---

#### ✅ Code implementation

```r
filteredData <- reactive({
  data <- iris  #Starting from the original data

  #Step 1: Filter by variety
  if (input$species != "total") {
    data <- data[data$Species == input$species, ]
  }

  #Step 2: Filter by corolla length range
  data <- data[data$Sepal.Length >= input$sepalLength[1] &
               data$Sepal.Length <= input$sepalLength[2], ]

  #Step 3: Filter by selected columns
  data <- data[, input$columns, drop = FALSE]

  #Step 4: Limit the number of rows displayed
  head(data, input$rows)
})
```

---

### 🧩 Module 2: Display table `output$table`

---

#### 🎯 Goal

Display the data filtered by the user in **table format** on the main interface.

---

#### 🧠 Explanation of ideas

`renderTable({...})` in Shiny will convert a `data.frame` into an HTML table and update it automatically.

---

#### ✅ Code implementation

```r
output$table <- renderTable({
  filteredData()  #Use the above reactive object
})
```

---

### 🧩 Module 3: Display summary information `output$summary`

---

#### 🎯 Goal

Display a "summary" of the data filtered by the user, for example:

```text
A total of 25 rows of data were filtered out
```

---

#### 🧠 Explanation of ideas

- Use `renderPrint()` to display plain text;
- Use `cat()` to implement multi-line formatting.

---

#### ✅ Code implementation

```r
output$summary <- renderPrint({
  data <- filteredData()
  cat("Totally screened out", nrow(data), "Transaction data")
})
```

---

### 🧩 Module 4: Implement download button `output$download`

---

#### 🎯 Goal

After the user clicks the download button, the current filter result is saved as a CSV file.

---

#### 🧠 Explanation of ideas

- use `downloadHandler()`;
- `filename = function()` specifies the file name;
- `content = function(file)` writes to file.

---

#### ✅ Code implementation

```r
output$download <- downloadHandler(
  filename = function() {
    paste("iris_filtered_", Sys.Date(), ".csv", sep = "")
  },
  content = function(file) {
    write.csv(filteredData(), file, row.names = FALSE)
  }
)
```

---

#### 🧱 Complete `server` build

```r
server <- function(input, output) {

  #1. Responsive filtering of data
  filteredData <- reactive({
    data <- iris
    if (input$species != "total") {
      data <- data[data$Species == input$species, ]
    }
    data <- data[data$Sepal.Length >= input$sepalLength[1] &
                 data$Sepal.Length <= input$sepalLength[2], ]
    data <- data[, input$columns, drop = FALSE]
    head(data, input$rows)
  })

  #2. Display the data table
  output$table <- renderTable({
    filteredData()
  })

  #3. Display summary information
  output$summary <- renderPrint({
    data <- filteredData()
    cat("Totally screened out", nrow(data), "Transaction data")
  })

  #4. Download function
  output$download <- downloadHandler(
    filename = function() {
      paste("iris_filtered_", Sys.Date(), ".csv", sep = "")
    },
    content = function(file) {
      write.csv(filteredData(), file, row.names = FALSE)
    }
  )
}
```

---

#### ✅ Summary: Complete item structure

|composition|Function description|
| --- | --- |
| `ui` |Define interface layout and control input and output locations|
| `server` |Define how the input is processed and how the output is generated|
| `shinyApp(ui, server)` |Launch the entire application|

---

#### 🚀 Launch the application

```r
shinyApp(ui = ui, server = server)
```

## 11. Today’s summary

### 11.1 List of input controls

**Text class:**

- `textInput()` - single line of text
- `textAreaInput()` - multi-line text (not covered today)
- `passwordInput()` - Password input (not discussed today)

**Number type:**

- `numericInput()` - Number input box
- `sliderInput()` - Slider

**Select Category:**

- `selectInput()` - drop-down box
- `radioButtons()` - radio button
- `checkboxInput()` - single checkbox
- `checkboxGroupInput()` - Checkbox group

**Date type:**

- `dateInput()` - single date
- `dateRangeInput()` - date range

**File class:**

- `fileInput()` - File upload

### 11.2 Remember these points

1. **All input controls require:**

   - `inputId` - unique identifier
   - `label` - Instructions displayed to the user
2. **Get the value in Server:**

   - Use `input$control_id`
   - Values are updated automatically
3. **Common parameters:**

   - `value` - Default value
   - `selected` - selected by default
   - `choices` - Options list
   - `min/max` - Min/Max

### 11.3 Choose appropriate controls

How to select controls

- Enter text → textInput
- Enter numbers → numericInput (exact) or sliderInput (fast)
- Choose one → radioButtons (less) or selectInput (more)
- Select multiple → checkboxGroupInput
- yes/no → checkboxInput
- date → dateInput
- file → fileInput

Congratulations on completing Day 3!

You've mastered all of Shiny's major input controls.
Tomorrow we will learn how to display various output results!

Homework

Create a "Personal Information Form" containing:

- Name (text)
- Age (number)
- Gender (single choice)
- Hobbies (multiple choices)
- Birthday (date)
- Introduction (text)
- Avatar (file upload)

And all the filled-in information is displayed on the right side.
