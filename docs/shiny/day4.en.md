# Day 4: Display results - present the analysis results elegantly

## 1. Understand the basic concepts of output

### 1.1 The relationship between input and output

In Shiny, the data flow is like this:

```text
User input → Server processing → Output display
```

Yesterday we learned about various input controls. Today we will learn how to display the output result.

### 1.2 Two steps of output

Each output requires two steps:

1. **Occupy position in UI**: Use `XXXOutput()`
2. **Generate content in Server**: use `renderXXX()`

These two must be used in pairs!

## 2. Text output: the simplest start

### 2.1 Understanding textOutput() and renderText()

Let’s first look at the syntax of these two functions:

```r
#UI end: occupy a position
textOutput(outputId = "mytext")

#Server side: generate content
output$mytext <- renderText({
  #Enter the text you want to display here.
})
```

**Key Points:**

- `outputId` must be consistent with the name after `output$`
- `renderText()` Use curly braces inside `{}`

### 2.2 First example: display the current time

Let's start with the simplest:

```r
library(shiny)

#Step 1: Create UI
ui <- fluidPage(
  h3("Display the current time"),
  textOutput("currentTime")  #Take a position, the ID is "currentTime"
)

#Step 2: Create Server
server <- function(input, output) {
  #Generate the content to be displayed
  output$currentTime <- renderText({
    paste("Now is:", Sys.time())
  })
}

#Step 3: Run
shinyApp(ui = ui, server = server)
```

### 2.3 Make text move: respond to user input

Now add user interaction:

```r
library(shiny)

ui <- fluidPage(
  h3("Text output exercise"),

  #Input part
  textInput("username", "Your name:"),
  sliderInput("age", "Your age:", 1, 100, 25),

  #Output part
  h4("Generated sentences:"),
  textOutput("sentence")
)

server <- function(input, output) {
  output$sentence <- renderText({
    #Build sentences
    #Note: We can use input$username and input$age.
    if(input$username == "") {
      "Please enter your name."
    } else {
      paste(input$username, "this year", input$age, "Years old.")
    }
  })
}

shinyApp(ui = ui, server = server)
```

### 2.4 verbatimTextOutput: Keep original format

Sometimes we want to keep the text in its original format (such as displaying code):

```r
library(shiny)

ui <- fluidPage(
  h3("The difference between the two types of text output"),

  h4("Normal text output textOutput:"),
  textOutput("normal"),

  h4("Original format output verbatimTextOutput:"),
  verbatimTextOutput("verbatim")
)

server <- function(input, output) {
  #The same content
  text_content <- "The first line is \n, the second line is \n, and there is a third line with indentation."

  output$normal <- renderText({
    text_content  #Newlines and spaces are ignored.
  })

  output$verbatim <- renderPrint({
    text_content  #Keep the original format
  })
}

shinyApp(ui = ui, server = server)
```

**When to use which one? **

- `textOutput` + `renderText`: Normal text display
- `verbatimTextOutput` + `renderPrint`: display code, data structure, retention format

## 3. Table output: display data

### 3.1 Basic tables: tableOutput() and renderTable()

Syntax structure:

```r
#UI end
tableOutput(outputId = "mytable")

#Server side
output$mytable <- renderTable({
  #Return a data.frame
})
```

### 3.2 The first table

Let's show some data:

```r
library(shiny)

ui <- fluidPage(
  h3("Basic form display"),

  #Use the slider to control how many rows are displayed.
  sliderInput("rows", "Display how many rows:", 1, 10, 5),

  #Table output location
  tableOutput("myTable")
)

server <- function(input, output) {
  output$myTable <- renderTable({
    #Use the built-in iris dataset
    #head() function takes the first few lines
    head(iris, input$rows)
  })
}

shinyApp(ui = ui, server = server)
```

### 3.3 Dynamically generate table content

Let's create a table that is dynamically generated based on user input:

```r
library(shiny)

ui <- fluidPage(
  h3("Transcript Generator"),

  #Enter student information
  textInput("name", "Student's name:", "Zhang San"),
  numericInput("chinese", "Chinese performance:", 85, 0, 100),
  numericInput("math", "Mathematics grades:", 90, 0, 100),
  numericInput("english", "English scores:", 88, 0, 100),

  hr(),

  #Show the transcript
  h4("Transcript:"),
  tableOutput("report")
)

server <- function(input, output) {
  output$report <- renderTable({
    #Create a data box
    scores <- data.frame(
      Subject = c("Language and Writing", "Mathematics", "English", "Total Score", "Average Score"),
      Score = c(
        input$chinese,
        input$math,
        input$english,
        input$chinese + input$math + input$english,
        round((input$chinese + input$math + input$english) / 3, 1)
      )
    )

    scores
  })
}

shinyApp(ui = ui, server = server)
```

### 3.4 Create interactive tables using the DT package

Ordinary tables have limited functionality, let's use the DT package to create more powerful tables:

```r
#Install the DT package first.
install.packages("DT")
```

```r
library(shiny)
library(DT)

ui <- fluidPage(
  h3("Interactive form"),

  #Note: Use DT::dataTableOutput instead of tableOutput.
  DT::dataTableOutput("interactiveTable")
)

server <- function(input, output) {
  #Note: Use DT::renderDataTable instead of renderTable.
  output$interactiveTable <- DT::renderDataTable({
    iris
  }, options = list(
    pageLength = 5,  #5 lines per page
    searching = TRUE  #Allow search
  ))
}

shinyApp(ui = ui, server = server)
```

**Advantages of DT tables:**

- Searchable
- Can be sorted
- Can be paginated
- Can choose how many rows to display

## 4. Graphic output: data visualization

### 4.1 Basic graphics: plotOutput() and renderPlot()

Syntax structure:

```r
#UI end
plotOutput(outputId = "myplot",
           width = "100%",    #Optional: Width
           height = "400px")  #Optional: Height

#Server side
output$myplot <- renderPlot({
  #Write and draw the code here.
  #You can use plot(), hist(), boxplot(), etc.
})
```

### 4.2 The first graph: histogram

```r
library(shiny)

ui <- fluidPage(
  h3("Histogram example"),

  #Control the parameters of the histogram
  sliderInput("bins", "Number of groups:", 5, 50, 30),
  selectInput("color", "Color:",
              choices = c("red" = "red",
                          "blue" = "blue",
                          "green" = "green")),

  #Graphic output
  plotOutput("histogram")
)

server <- function(input, output) {
  output$histogram <- renderPlot({
    #Generate random data
    data <- rnorm(1000)

    #Draw a histogram
    hist(data,
         breaks = input$bins,  #Use the number of groups selected by the user.
         col = input$color,    #Use the color selected by the user
         main = "Normal distribution histogram",
         xlab = "value",
         ylab = "frequent and successive")
  })
}

shinyApp(ui = ui, server = server)
```

### 4.3 Responsive data processing

When multiple outputs use the same data, use `reactive()` to avoid double counting:

```r
library(shiny)

ui <- fluidPage(
  h3("Data analysis instrument panel"),

  sidebarLayout(
    sidebarPanel(
      sliderInput("n", "Number of data points:", 50, 500, 100),
      numericInput("mean", "Average value:", 0),
      numericInput("sd", "Standard deviation:", 1, min = 0.1)
    ),

    mainPanel(
      #Multiple outputs
      plotOutput("histogram"),
      hr(),
      verbatimTextOutput("summary")
    )
  )
)

server <- function(input, output) {
  #Use reactive() to create responsive data
  #The data will be automatically updated when the input changes.
  myData <- reactive({
    rnorm(input$n, mean = input$mean, sd = input$sd)
  })

  #Output 1: Histogram
  output$histogram <- renderPlot({
    hist(myData(),  #Please pay attention to the parentheses!
         col = "lightblue",
         main = paste("Histogram (n =", input$n, ")"))
  })

  #Output 2: Statistical Summary
  output$summary <- renderPrint({
    data <- myData()  #Get data
    cat("Data summary: \n")
    cat("Sample quantity:", length(data), "\n")
    cat("Average value:", round(mean(data), 2), "\n")
    cat("Standard deviation:", round(sd(data), 2), "\n")
    cat("Minimum value:", round(min(data), 2), "\n")
    cat("Maximum value:", round(max(data), 2), "\n")
  })
}

shinyApp(ui = ui, server = server)
```

**Key points of programming thinking:**

- `reactive()` creates a "smart variable"
- It will listen for relevant input changes
- Remember to add brackets when using: `myData()`

### 4.4 Use ggplot2 to create more beautiful graphics

```r
library(shiny)
library(ggplot2)  #ggplot2 needs to be loaded first.

ui <- fluidPage(
  h3("ggplot2 graphics"),

  sidebarLayout(
    sidebarPanel(
      selectInput("xvar", "X-axis variable:",
                  choices = c("Sepal.Length", "Sepal.Width",
                              "Petal.Length", "Petal.Width")),
      selectInput("yvar", "Y-axis variable:",
                  choices = c("Sepal.Length", "Sepal.Width",
                              "Petal.Length", "Petal.Width"),
                  selected = "Sepal.Width")
    ),

    mainPanel(
      plotOutput("scatterplot")
    )
  )
)

server <- function(input, output) {
  output$scatterplot <- renderPlot({
    #Use ggplot2 syntax
    ggplot(iris, aes_string(x = input$xvar, y = input$yvar)) +
      geom_point(aes(color = Species), size = 3) +
      theme_minimal() +
      labs(title = paste(input$xvar, "vs", input$yvar))
  })
}

shinyApp(ui = ui, server = server)
```

## 5. Dynamic UI: uiOutput() and renderUI()

### 5.1 Why do we need dynamic UI?

Sometimes we need to dynamically change interface elements based on user selections.

Syntax structure:

```r
#UI end
uiOutput(outputId = "myui")

#Server side
output$myui <- renderUI({
  #Return to UI elements
})
```

### 5.2 Display different content based on conditions

```r
library(shiny)

ui <- fluidPage(
  h3("Example of dynamic interface"),

  radioButtons("choice", "You are:",
               choices = c("student", "teacher")),

  #Dynamic UI position
  uiOutput("dynamicUI"),

  #Show results
  textOutput("result")
)

server <- function(input, output) {
  #Generate different interfaces according to the selection.
  output$dynamicUI <- renderUI({
    if(input$choice == "student") {
      #The interface students see
      tagList(  #tagList is used to combine multiple UI elements
        textInput("studentID", "Student number:"),
        selectInput("grade", "Grade:",
                    choices = c("Freshman", "second year of college", "Senior year of college", "Senior year of college"))
      )
    } else {
      #The interface seen by the teacher
      tagList(
        textInput("teacherID", "Work number:"),
        selectInput("subject", "Subject:",
                    choices = c("mathematics", "language and writing", "English"))
      )
    }
  })

  #Display the information entered
  output$result <- renderText({
    if(input$choice == "student") {
      #Check whether the input in the student interface exists.
      if(!is.null(input$studentID)) {
        paste("student", input$studentID, "，", input$grade)
      }
    } else {
      #Check whether the input in the teacher interface exists.
      if(!is.null(input$teacherID)) {
        paste("teacher", input$teacherID, ", teach", input$subject)
      }
    }
  })
}

shinyApp(ui = ui, server = server)
```

**Key points of programming thinking:**

1. Use `tagList()` to combine multiple UI elements
2. The dynamically created input may not exist, please use `is.null()` to check
3. The interface will change in real time according to conditions

## 6. Download function: downloadButton() and downloadHandler()

### 6.1 Syntax of download function

```r
#UI end
downloadButton(outputId = "download",
               label = "download")

#Server side
output$download <- downloadHandler(
  filename = function() {
    #Generate file name
  },
  content = function(file) {
    #Generate file content
  }
)
```

### 6.2 Implement data download

Let's create an app that can download data:

```r
library(shiny)

ui <- fluidPage(
  h3("Data download example"),

  sidebarLayout(
    sidebarPanel(
      sliderInput("nrows", "Select the number of rows:", 1, 150, 10),

      radioButtons("filetype", "File format:",
                   choices = c("CSV" = "csv",
                               "text" = "txt")),

      br(),

      downloadButton("downloadData", "Download data")
    ),

    mainPanel(
      h4("Data preview:"),
      tableOutput("preview")
    )
  )
)

server <- function(input, output) {
  #Data to download
  datasetInput <- reactive({
    head(iris, input$nrows)
  })

  #Preview data
  output$preview <- renderTable({
    datasetInput()
  })

  #Download and process
  output$downloadData <- downloadHandler(
    #File name
    filename = function() {
      paste("iris_data_", Sys.Date(), ".", input$filetype, sep = "")
    },

    #File content
    content = function(file) {
      if(input$filetype == "csv") {
        write.csv(datasetInput(), file, row.names = FALSE)
      } else {
        write.table(datasetInput(), file, row.names = FALSE)
      }
    }
  )
}

shinyApp(ui = ui, server = server)
```

### 6.3 Download graphics

Not only can you download data, but you can also download graphics:

```r
library(shiny)
library(ggplot2)

ui <- fluidPage(
  h3("Graphic download example"),

  sidebarLayout(
    sidebarPanel(
      selectInput("plotType", "Graphic type:",
                  choices = c("Scatter plot", "Box diagram", "Histogram")),

      br(),

      downloadButton("downloadPlot", "Download the graphics")
    ),

    mainPanel(
      plotOutput("plot")
    )
  )
)

server <- function(input, output) {
  #Functions to create graphics
  makePlot <- function() {
    if(input$plotType == "Scatter plot") {
      ggplot(iris, aes(x = Sepal.Length, y = Sepal.Width, color = Species)) +
        geom_point(size = 3) +
        theme_minimal()
    } else if(input$plotType == "Box diagram") {
      ggplot(iris, aes(x = Species, y = Sepal.Length, fill = Species)) +
        geom_boxplot() +
        theme_minimal()
    } else {
      ggplot(iris, aes(x = Sepal.Length)) +
        geom_histogram(bins = 30, fill = "skyblue", color = "black") +
        theme_minimal()
    }
  }

  #Display graphics
  output$plot <- renderPlot({
    makePlot()
  })

  #Download the graphics
  output$downloadPlot <- downloadHandler(
    filename = function() {
      paste("plot_", Sys.Date(), ".png", sep = "")
    },

    content = function(file) {
      ggsave(file, plot = makePlot(), width = 8, height = 6)
    }
  )
}

shinyApp(ui = ui, server = server)
```

## 7. Comprehensive exercise: Data analysis report generator

Let’s put everything we learned today together:

```r
library(shiny)
library(ggplot2)
library(DT)

ui <- fluidPage(
  titlePanel("Data analysis report generator"),

  sidebarLayout(
    sidebarPanel(
      h4("Data selection"),
      selectInput("dataset", "Select the dataset:",
                  choices = c("Iris" = "iris",
                              "car" = "mtcars")),

      uiOutput("variableUI"),

      hr(),

      h4("Analysis options"),
      checkboxGroupInput("analysis", "Select the analysis content:",
                         choices = c("Data summary" = "summary",
                                     "Correlation analysis" = "correlation",
                                     "Distribution map" = "distribution",
                                     "Scatter plot" = "scatter"),
                         selected = c("summary", "distribution")),

      hr(),

      downloadButton("downloadReport", "Download the report")
    ),

    mainPanel(
      tabsetPanel(
        tabPanel("Data preview",
                 DT::dataTableOutput("dataTable")
        ),

        tabPanel("Analysis results",
                 uiOutput("analysisOutput")
        )
      )
    )
  )
)

server <- function(input, output) {
  #Get the selected dataset
  getDataset <- reactive({
    if(input$dataset == "iris") {
      iris
    } else {
      mtcars
    }
  })

  #Dynamically generate variable selection interface
  output$variableUI <- renderUI({
    data <- getDataset()
    numeric_vars <- names(data)[sapply(data, is.numeric)]

    tagList(
      selectInput("xvar", "X-axis variable:",
                  choices = numeric_vars),
      selectInput("yvar", "Y-axis variable:",
                  choices = numeric_vars,
                  selected = numeric_vars[2])
    )
  })

  #Data table
  output$dataTable <- DT::renderDataTable({
    getDataset()
  }, options = list(pageLength = 10))

  #Analysis output
  output$analysisOutput <- renderUI({
    output_list <- list()

    #Data summary
    if("summary" %in% input$analysis) {
      output$summaryText <- renderPrint({
        summary(getDataset())
      })
      output_list <- append(output_list, list(
        h4("Data summary"),
        verbatimTextOutput("summaryText"),
        hr()
      ))
    }

    #Correlation analysis
    if("correlation" %in% input$analysis && !is.null(input$xvar)) {
      output$corPlot <- renderPlot({
        data <- getDataset()
        numeric_data <- data[sapply(data, is.numeric)]
        cor_matrix <- cor(numeric_data)

        #Correlation heat map
        heatmap(cor_matrix,
                main = "Correlation heat map",
                margins = c(10, 10))
      })
      output_list <- append(output_list, list(
        h4("Correlation analysis"),
        plotOutput("corPlot"),
        hr()
      ))
    }

    #Distribution map
    if("distribution" %in% input$analysis && !is.null(input$xvar)) {
      output$distPlot <- renderPlot({
        ggplot(getDataset(), aes_string(x = input$xvar)) +
          geom_histogram(bins = 30, fill = "skyblue", color = "black") +
          theme_minimal() +
          labs(title = paste(input$xvar, "The distribution of"))
      })
      output_list <- append(output_list, list(
        h4("Distribution map"),
        plotOutput("distPlot"),
        hr()
      ))
    }

    #Scatter plot
    if("scatter" %in% input$analysis && !is.null(input$xvar) && !is.null(input$yvar)) {
      output$scatterPlot <- renderPlot({
        ggplot(getDataset(), aes_string(x = input$xvar, y = input$yvar)) +
          geom_point(size = 3, alpha = 0.7) +
          geom_smooth(method = "lm", se = TRUE) +
          theme_minimal() +
          labs(title = paste(input$xvar, "vs", input$yvar))
      })
      output_list <- append(output_list, list(
        h4("Scatter plot"),
        plotOutput("scatterPlot")
      ))
    }

    do.call(tagList, output_list)
  })

  #Download the report
  output$downloadReport <- downloadHandler(
    filename = function() {
      paste("data_report_", Sys.Date(), ".txt", sep = "")
    },

    content = function(file) {
      #Create report content
      sink(file)
      cat("Data analysis report \n")
      cat("Generation date:", as.character(Sys.Date()), "\n")
      cat("Data set:", input$dataset, "\n")
      cat("\n Data Summary: \n")
      print(summary(getDataset()))
      sink()
    }
  )
}

shinyApp(ui = ui, server = server)
```

## 8. Today’s summary

### 8.1 Output function pairing

|UI function|Server function|Purpose|
| --- | --- | --- |
| `textOutput()` | `renderText()` |display text|
| `verbatimTextOutput()` | `renderPrint()` |Show original text|
| `tableOutput()` | `renderTable()` |Show static table|
| `DT::dataTableOutput()` | `DT::renderDataTable()` |Show interactive table|
| `plotOutput()` | `renderPlot()` |display graphics|
| `uiOutput()` | `renderUI()` |Dynamically generate UI|
| `downloadButton()` | `downloadHandler()` |Download function|

### 8.2 Summary of programming thinking

1. **Decomposition thinking**:

   -Occupy a spot in the UI first
   - Then generate content on Server
   - finally connect
2. **Responsive Thinking**:

   - Use `reactive()` to avoid double counting
   - Understand the data flow: input → processing → output
3. **Dynamic Thinking**:

   - The interface can change according to conditions
   - Content can be updated based on input

### 8.3 Best Practices

1. **Name consistency**: The `outputId` name of the UI must be consistent with the `output$` name of the Server.
2. **CHECK FOR NULL**: Dynamically generated input may not exist
3. **Use reactive**: When multiple outputs use the same data
4. **Modularization**: Write complex graphics generation logic into functions

Day 4 completed!

You've mastered all of Shiny's main output methods.
Combined with the input controls from the previous three days, you can already create a fully functional Shiny application!

Today's homework

Create a "data explorer" that requires:
1. Can upload CSV files
2. Display the first few rows of data (adjustable)
3. Display basic statistical information
4. You can select two variables to draw a scatter plot
5. The processed data can be downloaded
