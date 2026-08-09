# Day 6: Practical item - data exploration tool

## 1. item planning: what we want to do

### 1.1 Requirements Analysis

We are going to make a data exploration tool with functions including:

1. **Upload function**: Users upload CSV files
2. **View function**: Preview data content
3. **Analysis function**: Generate statistical charts
4. **Download function**: Download analysis results

### 1.2 Development ideas

Instead of doing all the functions at once:

```text
Empty shell → Upload → Display → Analysis → Download → Beautification
```

Every step must work!

## 2. Step 1: Create the simplest framework

### 2.1 The most basic Shiny App

```r
library(shiny)

ui <- fluidPage(
  "Hello World"
)

server <- function(input, output) {
}

shinyApp(ui, server)
```

**Thinking Points:**

- Make sure Shiny is working properly first
- Start with the simplest

### 2.2 Add basic layout

```r
ui <- fluidPage(
  #Title
  titlePanel("Data exploration tool"),

  #Main layout
  sidebarLayout(
    #Left panel
    sidebarPanel(
      "Control area"
    ),

    #Right panel
    mainPanel(
      "Display area"
    )
  )
)
```

**Layout explanation:**

- `titlePanel()`: Page title
- `sidebarLayout()`: Sidebar layout (most commonly used)
- `sidebarPanel()`: Put controls
- `mainPanel()`: put result

## 3. Step 2: Add file upload function

### 3.1 Understanding fileInput()

```text
fileInput(
  inputId = "file", # ID, used for reference in the server
  label = "Select file:", #Displayed text
  accept = ".csv" # Restrict file types
)
```

### 3.2 Add upload control

```r
ui <- fluidPage(
  titlePanel("Data exploration tool"),

  sidebarLayout(
    sidebarPanel(
      #Add files and upload them.
      h4("Step 1: Upload data"),
      fileInput("file", "Select the CSV file:",
                accept = c(".csv", ".CSV")),

      #Separator line
      hr(),

      #Placeholder
      p("More controls will be added later...")
    ),

    mainPanel(
      h4("Data preview"),
      p("Please upload the file first.")
    )
  )
)
```

### 3.3 Test file upload

Test whether the file can be received in the server:

```r
server <- function(input, output) {
  #Monitor file uploads
  observe({
    #Print file information to the console
    print(input$file)
  })
}
```

**Test method:**

1. Run the app
2. Upload a CSV file
3. View the RStudio console

## 4. Step 3: Read the CSV file

### 4.1 Understanding reactive()

Why use `reactive()`?

```r
#Wrong method: direct reading
server <- function(input, output) {
  #This will cause an error!
  data <- read.csv(input$file$datapath)
}

#Correct way: use reactive
server <- function(input, output) {
  data <- reactive({
    read.csv(input$file$datapath)
  })
}
```

### 4.2 Read files safely

```r
server <- function(input, output) {
  #Reaction-based data reading
  data <- reactive({
    #Ensure that the document has been uploaded.
    req(input$file)

    #Read CSV
    read.csv(input$file$datapath,
             stringsAsFactors = FALSE)
  })
}
```

**Code explanation:**

- `req(input$file)`: Require file to exist, otherwise stop
- `stringsAsFactors = FALSE`: String is not converted to factors

### 4.3 Add error handling

```r
data <- reactive({
  req(input$file)

  #Try to read and capture possible errors.
  tryCatch({
    df <- read.csv(input$file$datapath,
                   stringsAsFactors = FALSE)
    df
  },
  error = function(e) {
    #If there is an error, return NULL.
    showNotification(
      "File reading failed. Please check the file format.",
      type = "error"
    )
    NULL
  })
})
```

## 5. Step 4: Display data preview

### 5.1 Add table output

Modify the main panel of the UI:

```text
mainPanel(
  h4("data preview"),
  #Add table output
  tableOutput("preview"),

  #Add information output
  hr(),
  h4("data information"),
  verbatimTextOutput("info")
)
```

### 5.2 Display the first few rows of data

```r
#Add in the server
output$preview <- renderTable({
  #Get data
  df <- data()

  #Display the first 10 lines
  head(df, 10)
})
```

### 5.3 Display basic information of data

```r
output$info <- renderPrint({
  df <- data()

  cat("📊 Dataset information \n")
  cat("=" , rep("=", 30), "\n", sep = "")
  cat("File name:", input$file$name, "\n")
  cat("File size:",
      round(input$file$size / 1024, 2), "KB\n")
  cat("Number of rows:", nrow(df), "\n")
  cat("Number of rows:", ncol(df), "\n")
  cat("\n column name: \n")
  for(i in 1:ncol(df)) {
    cat(i, ". ", names(df)[i],
        " (", class(df[[i]]), ")\n", sep = "")
  }
})
```

## 6. Step 5: Add column selection function

### 6.1 Why do we need dynamic UI?

Different CSV files have different column names, so the select boxes must be generated dynamically.

### 6.2 Create dynamic selection box

Add to the sidebar:

```text
sidebarPanel(
  h4("Step 1: Upload data"),
  fileInput("file", "Select CSV file:",
            accept = c(".csv", ".CSV")),

  hr(),

  # Dynamic UI placeholder
  h4("Step 2: Select analysis columns"),
  uiOutput("column_ui")
)
```

### 6.3 Generate selection box

```r
output$column_ui <- renderUI({
  #Data is needed first.
  req(data())

  #Get all column names
  choices <- names(data())

  #Create a dropdown
  selectInput("column",
              "Select the columns to analyze:",
              choices = choices)
})
```

### 6.4 Display only numerical columns

```r
output$column_ui <- renderUI({
  req(data())

  df <- data()
  #Find the numerical columns
  numeric_cols <- names(df)[sapply(df, is.numeric)]

  if(length(numeric_cols) == 0) {
    #No numeric columns
    p("⚠️ No numerical column was found.",
      style = "color: red;")
  } else {
    selectInput("column",
                "Select the columns to analyze:",
                choices = numeric_cols)
  }
})
```

## 7. Step 6: Add statistical analysis

### 7.1 Add analysis options

Continue adding in the dynamic UI:

```r
output$column_ui <- renderUI({
  req(data())

  df <- data()
  numeric_cols <- names(df)[sapply(df, is.numeric)]

  if(length(numeric_cols) == 0) {
    p("⚠️ No numerical column was found.", style = "color: red;")
  } else {
    tagList(  #Combine multiple UI elements
      selectInput("column",
                  "Select the columns to analyze:",
                  choices = numeric_cols),

      hr(),

      h4("Step 3: Select the analysis type"),
      radioButtons("plot_type",
                   "Chart type:",
                   choices = c("Histogram" = "hist",
                               "Box diagram" = "box",
                               "Density map" = "density"))
    )
  }
})
```

### 7.2 Organize content using tabs

Modify the main panel:

```text
mainPanel(
  tabsetPanel(
    # data labels
    tabPanel("Data Preview",
             br(),
             tableOutput("preview"),
             hr(),
             verbatimTextOutput("info")),

    # analyze tags
    tabPanel("Statistical Analysis",
             br(),
             plotOutput("plot"),
             hr(),
             verbatimTextOutput("summary"))
  )
)
```

### 7.3 Generate statistical charts

```r
output$plot <- renderPlot({
  #Ensure that the selected columns are
  req(input$column)

  #Get data from selected columns
  col_data <- data()[[input$column]]

  #Remove missing values
  col_data <- na.omit(col_data)

  #Draw according to your choice.
  if(input$plot_type == "hist") {
    hist(col_data,
         main = paste("Histogram:", input$column),
         xlab = input$column,
         col = "skyblue",
         border = "white")

  } else if(input$plot_type == "box") {
    boxplot(col_data,
            main = paste("Box diagram:", input$column),
            ylab = input$column,
            col = "lightgreen")

  } else if(input$plot_type == "density") {
    plot(density(col_data),
         main = paste("Density map:", input$column),
         xlab = input$column,
         lwd = 2,
         col = "red")
    polygon(density(col_data),
            col = rgb(1, 0, 0, 0.2))
  }
})
```

### 7.4 Add statistical summary

```r
output$summary <- renderPrint({
  req(input$column)

  col_data <- data()[[input$column]]

  cat("📈 Statistical summary:", input$column, "\n")
  cat("=" , rep("=", 40), "\n", sep = "")

  #Basic statistics
  cat("Sample quantity:", length(col_data), "\n")
  cat("Missing value:", sum(is.na(col_data)),
      "(", round(mean(is.na(col_data)) * 100, 1), "%)\n")

  #Effective value statistics
  valid_data <- na.omit(col_data)
  if(length(valid_data) > 0) {
    cat("\n valid value statistics: \n")
    cat("Minimum value:", min(valid_data), "\n")
    cat("The first quartile:", quantile(valid_data, 0.25), "\n")
    cat("Median:", median(valid_data), "\n")
    cat("Average value:", round(mean(valid_data), 2), "\n")
    cat("Third and fourth quartiles:", quantile(valid_data, 0.75), "\n")
    cat("Maximum value:", max(valid_data), "\n")
    cat("Standard deviation:", round(sd(valid_data), 2), "\n")
    cat("Variation coefficient:",
        round(sd(valid_data)/mean(valid_data), 3), "\n")
  }
})
```

## 8. Step 7: Add download function

### 8.1 Add download tab

```text
tabPanel("Download result",
         br(),
         h4("Download Options"),
         p("Select content to download:"),

         # Download data
         h5("📊 Original data"),
         downloadButton("download_data",
                        "Download CSV file"),

         br(), br(),

         # Download report
         h5("📄 Analysis Report"),
         downloadButton("download_report",
                        "Download analysis report"))
```

### 8.2 Implement data download

```r
output$download_data <- downloadHandler(
  #File name
  filename = function() {
    paste0("data_", Sys.Date(), ".csv")
  },

  #File content
  content = function(file) {
    write.csv(data(), file, row.names = FALSE)
  }
)
```

### 8.3 Implement report download

```r
output$download_report <- downloadHandler(
  filename = function() {
    paste0("report_", Sys.Date(), ".txt")
  },

  content = function(file) {
    #Open the file connection.
    sink(file)

    #Write the report content
    cat("Data analysis report \n")
    cat("=" , rep("=", 50), "\n\n", sep = "")

    cat("Generation time:", as.character(Sys.time()), "\n")
    cat("Analysis document:", input$file$name, "\n\n")

    #Data overview
    df <- data()
    cat("Data overview \n")
    cat("-" , rep("-", 30), "\n", sep = "")
    cat("Total number of branches:", nrow(df), "\n")
    cat("Total number of columns:", ncol(df), "\n")
    cat("Numerical column:", sum(sapply(df, is.numeric)), "\n")
    cat("Character string:", sum(sapply(df, is.character)), "\n\n")

    #If you select a column, add the analysis of the column.
    if(!is.null(input$column)) {
      cat("Column analysis:", input$column, "\n")
      cat("-" , rep("-", 30), "\n", sep = "")

      col_data <- df[[input$column]]
      valid_data <- na.omit(col_data)

      cat("Data type:", class(col_data), "\n")
      cat("Missing value:", sum(is.na(col_data)), "\n")
      cat("Minimum value:", min(valid_data), "\n")
      cat("Maximum value:", max(valid_data), "\n")
      cat("Average value:", mean(valid_data), "\n")
      cat("Standard deviation:", sd(valid_data), "\n")
    }

    #Close the file connection.
    sink()
  }
)
```

## 9. Step 8: Add data filtering function

### 9.1 Add filter control

In dynamic UI add:

```text
# Add after selecting the column
hr(),

h4("Step 4: Data filtering (optional)"),
checkboxInput("enable_filter",
              "Enable data filtering"),

conditionalPanel(
  condition = "input.enable_filter == true",
  uiOutput("filter_ui")
)
```

### 9.2 Generate filtering interface

```r
output$filter_ui <- renderUI({
  req(input$column)

  col_data <- data()[[input$column]]

  tagList(
    sliderInput("filter_range",
                "Select the range of values:",
                min = min(col_data, na.rm = TRUE),
                max = max(col_data, na.rm = TRUE),
                value = c(min(col_data, na.rm = TRUE),
                          max(col_data, na.rm = TRUE))),

    textOutput("filter_info")
  )
})
```

### 9.3 Apply filtering

Create filtered data:

```r
#Filtered data
filtered_data <- reactive({
  df <- data()

  if(input$enable_filter && !is.null(input$filter_range)) {
    #Application filtering
    df <- df[df[[input$column]] >= input$filter_range[1] &
             df[[input$column]] <= input$filter_range[2], ]
  }

  df
})

#Show filtering information
output$filter_info <- renderText({
  if(input$enable_filter) {
    paste("Remaining after screening", nrow(filtered_data()), "line")
  }
})
```

## 10. Complete code (with detailed comments)

```r
#Load the necessary packages
library(shiny)

#========== UI Part ==========
ui <- fluidPage(
  #Application title
  titlePanel("Data exploration tool v1.0"),

  #Add instructions
  tags$div(
    class = "alert alert-info",
    tags$strong("Instructions for use:"),
    "Upload CSV file → Select analysis columns → View statistical charts → Download results"
  ),

  #Main layout: sidebar layout
  sidebarLayout(
    #===== Sidebar Panel =====
    sidebarPanel(
      #Step 1: Upload the file
      tags$div(
        class = "well",
        h4("📁 Step 1: Upload data"),
        fileInput("file",
                  "Select the CSV file:",
                  accept = c(".csv", ".CSV"),
                  buttonLabel = "Browse...",
                  placeholder = "No file selected")
      ),

      #Separator line
      hr(),

      #Dynamic UI: Generate controls according to uploaded files
      uiOutput("column_ui"),

      #Add some instructions.
      br(),
      tags$small(
        class = "text-muted",
        "Tips: Only numerical columns can be used for statistical analysis."
      )
    ),

    #===== Main panel =====
    mainPanel(
      #Organize different functions with tabs
      tabsetPanel(
        id = "tabs",

        #Tag 1: Data preview
        tabPanel("Data preview",
                 value = "preview_tab",
                 br(),
                 #Display basic information of the data
                 verbatimTextOutput("info"),
                 hr(),
                 #Display data table
                 h4("The first 10 lines of data"),
                 tableOutput("preview")
        ),

        #Label 2: Statistical analysis
        tabPanel("Statistical analysis",
                 value = "analysis_tab",
                 br(),
                 #Statistical charts
                 plotOutput("plot", height = "400px"),
                 hr(),
                 #Statistical summary
                 verbatimTextOutput("summary")
        ),

        #Tag 3: Download results
        tabPanel("Download results",
                 value = "download_tab",
                 br(),
                 h4("📥 Download options"),

                 #Download the original data
                 tags$div(
                   class = "well",
                   h5("raw data"),
                   p("Download and upload the downloaded CSV file."),
                   downloadButton("download_data",
                                  "Download CSV",
                                  class = "btn-primary")
                 ),

                 #Download the analysis report
                 tags$div(
                   class = "well",
                   h5("Analysis report"),
                   p("Download the text report of data analysis"),
                   downloadButton("download_report",
                                  "Download the report",
                                  class = "btn-success")
                 )
        )
      )
    )
  )
)

#========== Server Part ==========
server <- function(input, output, session) {

  #===== Reaction expression =====

  #Read the uploaded CSV file
  data <- reactive({
    #Ensure that the document has been uploaded.
    req(input$file)

    #Show progress bar
    withProgress(message = 'Reading the file...', value = 0, {
      #Update progress
      incProgress(0.3, detail = "Reading...")

      #Try to read the file and handle possible errors.
      tryCatch({
        #Read CSV
        df <- read.csv(input$file$datapath,
                       stringsAsFactors = FALSE,
                       fileEncoding = "UTF-8")

        #Update progress
        incProgress(0.7, detail = "Processing...")

        #Return to the data box
        df

      }, error = function(e) {
        #Display an error message if an error occurs.
        showNotification(
          paste("File reading error:", e$message),
          type = "error",
          duration = 5
        )
        return(NULL)
      })
    })
  })

  #===== Output part =====

  #Display data information
  output$info <- renderPrint({
    #Ensure data has loaded
    req(data())

    df <- data()

    cat("📊 Dataset information \n")
    cat(strrep("=", 50), "\n")
    cat("File name:", input$file$name, "\n")
    cat("File size:",
        round(input$file$size / 1024, 2), "KB\n")
    cat("Encoding: UTF-8\n")
    cat("\n")
    cat("Data dimension \n")
    cat(strrep("-", 30), "\n")
    cat("Number of rows:", nrow(df), "\n")
    cat("Number of rows:", ncol(df), "\n")
    cat("\n")
    cat("List information \n")
    cat(strrep("-", 30), "\n")

    #Display information for each column
    for(i in 1:ncol(df)) {
      col_name <- names(df)[i]
      col_type <- class(df[[i]])[1]
      na_count <- sum(is.na(df[[i]]))
      na_pct <- round(na_count / nrow(df) * 100, 1)

      cat(sprintf("%2d. %-20s %-10s Missing value: %d (%.1f%%)\n",
                  i, col_name, col_type, na_count, na_pct))
    }
  })

  #Display data preview
  output$preview <- renderTable({
    req(data())

    #Display the first 10 lines, and if there are fewer than 10 lines, display all of them.
    head(data(), min(10, nrow(data())))
  },
  striped = TRUE,      #striped table
  hover = TRUE,        #Mouse hover effect
  bordered = TRUE      #Borders
  )

  #Dynamic generation of column selection UI
  output$column_ui <- renderUI({
    #Data is needed first.
    req(data())

    df <- data()

    #Find all numerical columns
    numeric_cols <- names(df)[sapply(df, is.numeric)]

    #Check for numeric columns
    if(length(numeric_cols) == 0) {
      #No prompt when there is no numeric column
      tags$div(
        class = "alert alert-warning",
        tags$strong("Note:"),
        "No numerical columns were found in the data, so statistical analysis cannot be carried out."
      )
    } else {
      #Generate a selection interface when there is a numerical column.
      tagList(
        tags$div(
          class = "well",
          h4("📊 Step 2: Select the analysis column"),
          selectInput("column",
                      "Select the columns to analyze:",
                      choices = numeric_cols,
                      selected = numeric_cols[1])
        ),

        hr(),

        tags$div(
          class = "well",
          h4("📈 Step 3: Select the analysis type"),
          radioButtons("plot_type",
                       "Chart type:",
                       choices = list(
                         "Histogram" = "hist",
                         "Box diagram" = "box",
                         "Density map" = "density",
                         "QQ picture" = "qq"
                       ),
                       selected = "hist")
        ),

        hr(),

        #Data filtering options
        tags$div(
          class = "well",
          h4("🔍 Step 4: Data screening (optional)"),
          checkboxInput("enable_filter",
                        "Enable data filtering",
                        value = FALSE),

          #Condition Panel: Only displayed when filtering is enabled
          conditionalPanel(
            condition = "input.enable_filter == true",
            uiOutput("filter_ui")
          )
        )
      )
    }
  })

  #Generate filter UI
  output$filter_ui <- renderUI({
    req(input$column)

    col_data <- data()[[input$column]]
    col_data <- na.omit(col_data)

    if(length(col_data) > 0) {
      tagList(
        sliderInput("filter_range",
                    "Select the range of values:",
                    min = min(col_data),
                    max = max(col_data),
                    value = c(min(col_data), max(col_data)),
                    step = (max(col_data) - min(col_data)) / 100),

        tags$small(
          class = "text-info",
          textOutput("filter_info")
        )
      )
    }
  })

  #Filtered data
  filtered_data <- reactive({
    df <- data()

    #If filtering is enabled and a range is set
    if(!is.null(input$enable_filter) &&
       input$enable_filter &&
       !is.null(input$filter_range) &&
       !is.null(input$column)) {

      #Data retained within scope
      keep_rows <- df[[input$column]] >= input$filter_range[1] &
                   df[[input$column]] <= input$filter_range[2]
      keep_rows[is.na(keep_rows)] <- FALSE

      df <- df[keep_rows, ]
    }

    df
  })

  #Show filtering information
  output$filter_info <- renderText({
    if(!is.null(input$enable_filter) && input$enable_filter) {
      total <- nrow(data())
      filtered <- nrow(filtered_data())
      paste0("After screening:", filtered, " / ", total, "OK",
             "(", round(filtered/total*100, 1), "%)")
    }
  })

  #Generate statistical charts and graphs
  output$plot <- renderPlot({
    #Ensure that the selected columns are
    req(input$column)

    #Get data
    df <- filtered_data()
    col_data <- df[[input$column]]

    #Remove missing values
    col_data <- na.omit(col_data)

    #Check for valid data
    if(length(col_data) == 0) {
      plot(1, type = "n", axes = FALSE,
           xlab = "", ylab = "")
      text(1, 1, "There are no valid data to draw.",
           cex = 1.5, col = "gray")
      return()
    }

    #Set graphic parameters
    par(mar = c(4, 4, 3, 2))

    #Draw according to the selected type.
    if(input$plot_type == "hist") {
      #Histogram
      hist(col_data,
           breaks = "Sturges",  #Automatically determine the number of groups
           main = paste("Histogram:", input$column),
           xlab = input$column,
           ylab = "frequent and successive",
           col = "skyblue",
           border = "white")

      #Add a normal distribution curve
      x <- seq(min(col_data), max(col_data), length.out = 100)
      y <- dnorm(x, mean = mean(col_data), sd = sd(col_data))
      y <- y * length(col_data) * diff(range(col_data)) / 30
      lines(x, y, col = "red", lwd = 2)

      #Add a mean line
      abline(v = mean(col_data), col = "red",
             lwd = 2, lty = 2)

      #Legend
      legend("topright",
             legend = c("data", "Normal curve", "mean value"),
             col = c("skyblue", "red", "red"),
             lty = c(0, 1, 2),
             pch = c(15, NA, NA),
             lwd = c(NA, 2, 2))

    } else if(input$plot_type == "box") {
      #Box diagram
      boxplot(col_data,
              main = paste("Box diagram:", input$column),
              ylab = input$column,
              col = "lightgreen",
              border = "darkgreen",
              notch = TRUE,  #Display groove
              outline = TRUE)  #Display abnormal values

      #Add the mean point
      points(1, mean(col_data),
             col = "red", pch = 19, cex = 1.5)

      #Add data points (shake)
      points(jitter(rep(1, length(col_data)), 0.2),
             col_data,
             col = rgb(0, 0, 0, 0.2),
             pch = 19, cex = 0.5)

    } else if(input$plot_type == "density") {
      #Density map
      d <- density(col_data)
      plot(d,
           main = paste("Density map:", input$column),
           xlab = input$column,
           ylab = "density",
           lwd = 2,
           col = "blue")

      #Filling area
      polygon(d, col = rgb(0, 0, 1, 0.2))

      #Add mean and median lines
      abline(v = mean(col_data),
             col = "red", lwd = 2, lty = 2)
      abline(v = median(col_data),
             col = "green", lwd = 2, lty = 2)

      #Legend
      legend("topright",
             legend = c("Density curve", "mean value", "median"),
             col = c("blue", "red", "green"),
             lty = c(1, 2, 2),
             lwd = 2)

    } else if(input$plot_type == "qq") {
      #QQ picture
      qqnorm(col_data,
             main = paste("QQ picture:", input$column),
             xlab = "Theoretical percentile",
             ylab = "Sample percentile",
             pch = 19,
             col = "darkblue")
      qqline(col_data, col = "red", lwd = 2)

      #Addition instructions
      legend("topleft",
             legend = c("Data point", "Reference line"),
             col = c("darkblue", "red"),
             pch = c(19, NA),
             lty = c(NA, 1),
             lwd = c(NA, 2))
    }

    #Add grid
    grid(col = "lightgray", lty = "dotted")
  })

  #Show statistical summary
  output$summary <- renderPrint({
    req(input$column)

    #Get data
    df <- filtered_data()
    col_data <- df[[input$column]]

    cat("📈 Statistical summary:", input$column, "\n")
    cat(strrep("=", 50), "\n\n")

    #Sample information
    cat("Sample information \n")
    cat(strrep("-", 30), "\n")
    cat("Total sample size:", length(col_data), "\n")
    cat("Missing value:", sum(is.na(col_data)),
        sprintf("(%.1f%%)", mean(is.na(col_data)) * 100), "\n")
    cat("Effective value:", sum(!is.na(col_data)), "\n\n")

    #Calculate the statistics of valid data
    valid_data <- na.omit(col_data)

    if(length(valid_data) > 0) {
      #Centralized trend
      cat("Centralized Trend \n")
      cat(strrep("-", 30), "\n")
      cat("Minimum value:", min(valid_data), "\n")
      cat("The first quartile:", quantile(valid_data, 0.25), "\n")
      cat("Median:", median(valid_data), "\n")
      cat("Average value:", mean(valid_data), "\n")
      cat("Third and fourth quartiles:", quantile(valid_data, 0.75), "\n")
      cat("Maximum value:", max(valid_data), "\n\n")

      #Discrete degree
      cat("Discrete degree \n")
      cat(strrep("-", 30), "\n")
      cat("Extremely poor:", max(valid_data) - min(valid_data), "\n")
      cat("Quartile distance:", IQR(valid_data), "\n")
      cat("Variance:", var(valid_data), "\n")
      cat("Standard deviation:", sd(valid_data), "\n")
      cat("Standard error:", sd(valid_data)/sqrt(length(valid_data)), "\n")
      cat("Variation coefficient:", sd(valid_data)/mean(valid_data), "\n\n")

      #Distribution form
      cat("Distribution morphology \n")
      cat(strrep("-", 30), "\n")

      #Calculate the tilt and peak angle
      n <- length(valid_data)
      m <- mean(valid_data)
      s <- sd(valid_data)

      skew <- sum((valid_data - m)^3) / (n * s^3)
      kurt <- sum((valid_data - m)^4) / (n * s^4) - 3

      cat("Tilt:", round(skew, 3),
          ifelse(abs(skew) < 0.5, "(Approximate symmetry)",
                 ifelse(skew > 0, "(Right-biased)", "(Left-biased)")), "\n")
      cat("Peak degree:", round(kurt, 3),
          ifelse(abs(kurt) < 0.5, "(Approximately normal)",
                 ifelse(kurt > 0, "(Peak)", "(Pingfeng)")), "\n")

      #Normality test (if the sample size is appropriate)
      if(length(valid_data) >= 3 && length(valid_data) <= 5000) {
        sw_test <- shapiro.test(valid_data)
        cat("\nShapiro-Wilk normality test \n")
        cat(strrep("-", 30), "\n")
        cat("W statistics:", round(sw_test$statistic, 4), "\n")
        cat("p value:", round(sw_test$p.value, 4), "\n")
        cat("Conclusion:", ifelse(sw_test$p.value > 0.05,
                           "The normality assumption cannot be rejected.",
                           "Reject the normality assumption"), "\n")
      }
    } else {
      cat("There are no valid data for statistical analysis \n")
    }
  })

  #===== Download function =====

  #Download data
  output$download_data <- downloadHandler(
    filename = function() {
      #Generated file name: original file name_filtered_date.csv
      base_name <- tools::file_path_sans_ext(input$file$name)
      if(!is.null(input$enable_filter) && input$enable_filter) {
        paste0(base_name, "_filtered_", Sys.Date(), ".csv")
      } else {
        paste0(base_name, "_", Sys.Date(), ".csv")
      }
    },

    content = function(file) {
      #Write to CSV file
      write.csv(filtered_data(),
                file,
                row.names = FALSE,
                fileEncoding = "UTF-8")

      #Display a success notification
      showNotification("Data download successful!",
                       type = "success",
                       duration = 3)
    }
  )

  #Download the report
  output$download_report <- downloadHandler(
    filename = function() {
      #Generate report file name
      base_name <- tools::file_path_sans_ext(input$file$name)
      paste0("report_", base_name, "_", Sys.Date(), ".txt")
    },

    content = function(file) {
      #Create report content
      sink(file)

      cat("Data analysis report \n")
      cat(strrep("=", 60), "\n\n")

      #Basic information
      cat("Report information \n")
      cat(strrep("-", 40), "\n")
      cat("Generation time:", format(Sys.time(), "%Y-%m-%d %H:%M:%S"), "\n")
      cat("Analysis tool: Data exploration tool v1.0\n")
      cat("Operating system:", Sys.info()["sysname"], "\n")
      cat("R version:", R.version.string, "\n\n")

      #File information
      cat("File information \n")
      cat(strrep("-", 40), "\n")
      cat("File name:", input$file$name, "\n")
      cat("File size:", round(input$file$size / 1024, 2), "KB\n")
      cat("Upload time:",
          format(file.info(input$file$datapath)$mtime,
                 "%Y-%m-%d %H:%M:%S"), "\n\n")

      #Data overview
      df <- data()
      cat("Data overview \n")
      cat(strrep("-", 40), "\n")
      cat("Total number of branches:", nrow(df), "\n")
      cat("Total number of columns:", ncol(df), "\n")
      cat("Numerical columns:", sum(sapply(df, is.numeric)), "\n")
      cat("Character type column:", sum(sapply(df, is.character)), "\n")
      cat("Logical type column:", sum(sapply(df, is.logical)), "\n\n")

      #Row details
      cat("List detailed information \n")
      cat(strrep("-", 40), "\n")
      for(i in 1:ncol(df)) {
        col_name <- names(df)[i]
        col_type <- class(df[[i]])[1]
        na_count <- sum(is.na(df[[i]]))
        na_pct <- round(na_count / nrow(df) * 100, 1)

        cat(sprintf("%2d. %-20s Type:%-10s Missing::%d(%.1f%%)\n",
                    i, col_name, col_type, na_count, na_pct))
      }

      #Add a detailed analysis if you select a specific column.
      if(!is.null(input$column)) {
        cat("\n\n")
        cat("Selected column analysis:", input$column, "\n")
        cat(strrep("=", 60), "\n\n")

        col_data <- df[[input$column]]
        valid_data <- na.omit(col_data)

        #Basic statistics
        cat("Descriptive statistics \n")
        cat(strrep("-", 40), "\n")
        cat("Sample quantity:", length(col_data), "\n")
        cat("Missing value:", sum(is.na(col_data)), "\n")
        cat("Effective value:", length(valid_data), "\n\n")

        if(length(valid_data) > 0) {
          #Five-number summary
          fivenum_vals <- fivenum(valid_data)
          cat("Five-digit summary \n")
          cat(strrep("-", 40), "\n")
          cat("Minimum value:", fivenum_vals[1], "\n")
          cat("The first quartile:", fivenum_vals[2], "\n")
          cat("Median:", fivenum_vals[3], "\n")
          cat("Third and fourth quartiles:", fivenum_vals[4], "\n")
          cat("Maximum value:", fivenum_vals[5], "\n\n")

          #Other statistics
          cat("Other statistics \n")
          cat(strrep("-", 40), "\n")
          cat("Average value:", mean(valid_data), "\n")
          cat("Standard deviation:", sd(valid_data), "\n")
          cat("Variance:", var(valid_data), "\n")
          cat("Standard error:", sd(valid_data)/sqrt(length(valid_data)), "\n")
          cat("Variation coefficient:", sd(valid_data)/mean(valid_data), "\n")
          cat("Extremely poor:", max(valid_data) - min(valid_data), "\n")
          cat("Quartile distance:", IQR(valid_data), "\n")

          #Add filter information if filtering is enabled.
          if(!is.null(input$enable_filter) && input$enable_filter) {
            cat("\n Filtering Information \n")
            cat(strrep("-", 40), "\n")
            cat("Screening scope: [", input$filter_range[1],
                ", ", input$filter_range[2], "]\n")
            cat("Number of steps to be filtered:", nrow(df), "\n")
            cat("Number of rows after screening:", nrow(filtered_data()), "\n")
            cat("Retention ratio:",
                round(nrow(filtered_data())/nrow(df)*100, 1), "%\n")
          }
        }
      }

      #Closing words
      cat("\n\n")
      cat(strrep("-", 60), "\n")
      cat("Report ends \n")

      sink()

      #Display a success notification
      showNotification("Report generation successful!",
                       type = "success",
                       duration = 3)
    }
  )

  #===== Other functions =====

  #Automatically switch to Preview tab when the file is uploaded
  observeEvent(input$file, {
    updateTabsetPanel(session, "tabs", selected = "preview_tab")
  })

  #Automatically switches to the Analysis tab after selecting a column
  observeEvent(input$column, {
    if(!is.null(input$column)) {
      updateTabsetPanel(session, "tabs", selected = "analysis_tab")
    }
  })
}

#========== Run the application ==========
shinyApp(ui = ui, server = server)
```

## 11. item summary

### 11.1 What we learned

Through this item, we have mastered:

1. **item development process**:

   - Requirements analysis
   - Implemented step by step
   - Test optimization
2. **Core technical points**:

   - File upload processing
   - Dynamic UI generation
   - Data visualization
   - Download function
3. **Actual problem handling**:

   - error handling
   - User experience
   - Code organization

### 11.2 Areas that can continue to be improved

1. **Support more file formats**:

   - Excel file (.xlsx)
   - JSON file
   - text file
2. **More analysis functions**:

   - Correlation analysis
   - Multivariate analysis
   - Time series analysis
3. **Better user experience**:

   - Data preprocessing options
   - Chart customization
   - Batch processing

### 11.3 Key programming thinking

1. **Modular thinking**: Each function is implemented independently
2. **User Thinking**: Design from the user’s perspective
3. **Robust Thinking**: Handle various abnormal situations
4. **Iterative Thinking**: Continuous Improvement and Optimization

item completed!

You've created a fully functional data exploration tool.
This tool can really be used for daily data analysis work.

Suggestions for next steps

1. Test the tool on your own data
2. Add new features as needed
3. Share it with those who need it
4. Open source your improved version on GitHub
