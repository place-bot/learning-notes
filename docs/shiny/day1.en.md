# Day 1: Hello World - Get your first Shiny App running

## 1. Preparation before starting

### 1.1 Install Shiny package

Open RStudio and enter in the console:

```r
install.packages("shiny")
```

After the installation is complete, test it:

```r
library(shiny)
```

If no error is reported, the installation is successful!

### 1.2 Understand two core concepts

Before we start writing code, we need to understand the two core parts of Shiny:

**UI (User Interface):**

- It’s what you can see on the web page
- Buttons, text, pictures, etc.

**Server:**

- This is where data is processed in the background
- Invisible to users, but working silently

Simple to understand

The UI is like the front lobby of a restaurant (what guests can see)
Server is like the back kitchen of a restaurant (the place where food is cooked)

## 2. First example: the simplest App

### 2.1 Create new file

In RStudio:

1. File → New File → Shiny Web App
2. Give it a name, such as "my_first_app"
3. Select "Single File"
4. Click Create

RStudio automatically generates a template; this section starts with an empty file to understand the minimal structure.

### 2.2 Minimal Hello World example

Delete all the code and enter the following:

```r
library(shiny)

#UI part
ui <- fluidPage(
  "Hello World!"
)

#Server part
server <- function(input, output) {
  #Do nothing here.
}

#Run the app
shinyApp(ui = ui, server = server)
```

Click the "Run App" button in the upper right corner, and you will see a webpage that displays "Hello World!"!

Code explanation

- `library(shiny)` - Load Shiny package
- `ui <- fluidPage()` - Create a web page
- `server <- function()` - Create background processing function
- `shinyApp()` - Combine UI and Server to run

## 3. Add some spice: add a title

### 3.1 Add a big title

```r
library(shiny)

ui <- fluidPage(
  h1("My first Shiny App"),  #h1 is a first-level title.
  p("This is a paragraph of text.")         #p is a paragraph
)

server <- function(input, output) {
}

shinyApp(ui = ui, server = server)
```

### 3.2 Example of multi-level title

```r
library(shiny)

ui <- fluidPage(
  h1("Level 1 title - maximum"),
  h2("Secondary title - the second largest"),
  h3("Level 3 title - Intermediate"),
  h4("Level 4 title - smaller"),
  p("Ordinary paragraph text"),
  br(),  #Line break
  p("This is another paragraph.")
)

server <- function(input, output) {
}

shinyApp(ui = ui, server = server)
```

HTML tag

These HTML tags can be used in Shiny:

- `h1()` to `h6()` - Title (1 maximum, 6 minimum)
- `p()` - Paragraph
- `br()` - Line feed
- `strong()` - bold
- `em()` - italic

## 4. The first interaction: button and text

### 4.1 Add a button

Add an example of a button event below: display text after clicking the button.

```r
library(shiny)

ui <- fluidPage(
  h1("Click the button to test"),

  #Add a button
  actionButton("button1", "Running example"),

  #Where the text is displayed
  textOutput("text1")
)

server <- function(input, output) {
  #When the button is clicked
  observeEvent(input$button1, {
    output$text1 <- renderText({
      "You clicked the button!"
    })
  })
}

shinyApp(ui = ui, server = server)
```

After running, click the button to display the text.

### 4.2 Understand this example

Let us understand step by step:

**UI part:**

- `actionButton("button1", "Run Example")` - Create a button

  - `"button1"` is the ID (ID card) of this button
  - `"Run Example"` is the text displayed on the button
- `textOutput("text1")` - Create a place to display text

  - `"text1"` is the ID of this output

**Server part:**

- `observeEvent(input$button1, {...})` - Monitor button clicks

  - `input$button1` Get the status of the button
- `output$text1 <- renderText({...})` - Output text

  - `output$text1` corresponds to `textOutput("text1")` in the UI

Remember this pattern

1. Use `XXXInput()` to create an input (such as a button) in the UI
2. Use `XXXOutput()` in the UI to create the output location
3. Use `input$ID` in Server to obtain input
4. Use `output$ID <- renderXXX()` in Server to create output

## 5. More interesting example: slider to control numbers

### 5.1 Basic version

```r
library(shiny)

ui <- fluidPage(
  h1("Slider controller"),

  #Create a slider
  sliderInput("slider1",
              "Choose a number:",
              min = 1,
              max = 100,
              value = 50),

  #Display the selected number
  textOutput("number1")
)

server <- function(input, output) {
  #Display the value of the slider
  output$number1 <- renderText({
    paste("You have chosen:", input$slider1)
  })
}

shinyApp(ui = ui, server = server)
```

### 5.2 upgraded version: slider control graphics

```r
library(shiny)

ui <- fluidPage(
  h1("Slider control histogram"),

  #Sidebar layout
  sidebarLayout(
    #Controls in the sidebar
    sidebarPanel(
      sliderInput("bins",
                  "Select the number of groups for the histogram:",
                  min = 1,
                  max = 50,
                  value = 30)
    ),

    #Put the picture on the main panel.
    mainPanel(
      plotOutput("distPlot")
    )
  )
)

server <- function(input, output) {
  output$distPlot <- renderPlot({
    #Generate data
    x <- rnorm(1000)

    #Draw a histogram
    hist(x,
         breaks = input$bins,  #Use the value of the slider
         col = 'lightblue',
         border = 'white',
         main = paste("Histogram (", input$bins, "Group)"))
  })
}

shinyApp(ui = ui, server = server)
```

Run this example, drag the slider, and the graph will change in real time!

## 6. Common errors and solutions

### 6.1 Error: could not find function

```r
#Error example
ui <- fluidPage(
  sliderInput("test", "test", 1, 100, 50)
)

#Solution: Remember to load the package first.
library(shiny)
```

### 6.2 Error: object 'input' not found

```r
#Error example
ui <- fluidPage(
  textOutput("text1")
)

server <- function(input, output) {
  output$text1 <- renderText({
    input$slider1  #But slider1 was not created in the UI!
  })
}

#Solution: Ensure that there are corresponding input controls in the UI.
```

### 6.3 Error: Duplicate ID

```r
#Error example
ui <- fluidPage(
  sliderInput("id1", "Slider 1", 1, 100, 50),
  sliderInput("id1", "Slider 2", 1, 100, 50)  #ID has been repeated!
)

#Resolution: The ID of each control must be unique
ui <- fluidPage(
  sliderInput("id1", "Slider 1", 1, 100, 50),
  sliderInput("id2", "Slider 2", 1, 100, 50)  #Change to a different ID
)
```

## 7. Practice time

### 7.1 Exercise 1: Text input

Create an app where the user enters their name and displays "Hello, XXX!"

```r
library(shiny)

ui <- fluidPage(
  h1("Greetings program"),

  #Tips: Use textInput()
  textInput("name", "Please enter your name:"),

  #Display greeting message
  textOutput("greeting")
)

server <- function(input, output) {
  output$greeting <- renderText({
    #Tip: Use paste() to combine text.
    paste("Hello,", input$name, "！")
  })
}

shinyApp(ui = ui, server = server)
```

### 7.2 Exercise 2: Multiple Controls

Create an app with two sliders that display their sum:

```r
library(shiny)

ui <- fluidPage(
  h1("Addition calculator"),

  sliderInput("num1", "The first number:", 0, 100, 50),
  sliderInput("num2", "The second number:", 0, 100, 50),

  h3("Result:"),
  textOutput("sum")
)

server <- function(input, output) {
  output$sum <- renderText({
    #Calculate the sum of two numbers
    result <- input$num1 + input$num2
    paste(input$num1, "+", input$num2, "=", result)
  })
}

shinyApp(ui = ui, server = server)
```

### 7.3 Exercise 3: Conditional display

Display different messages depending on the value of the slider:

```r
library(shiny)

ui <- fluidPage(
  h1("thermograph"),

  sliderInput("temp", "Current temperature:", -10, 40, 20),

  textOutput("message")
)

server <- function(input, output) {
  output$message <- renderText({
    if (input$temp < 0) {
      "It's too cold!❄️"
    } else if (input$temp < 15) {
      "It's a little cold 🧥"
    } else if (input$temp < 25) {
      "Very comfortable 😊"
    } else if (input$temp < 35) {
      "It's a little hot 🌞"
    } else {
      "It's too hot! 🔥"
    }
  })
}

shinyApp(ui = ui, server = server)
```

## 8. Today’s summary

### 8.1 What have you learned?

1. **Basic structure:**
   UI + Server + `shinyApp()`
2. **Commonly used UI controls:**

   - `actionButton()` – Button
   - `sliderInput()` – Slider
   - `textInput()` – Text input
   - `textOutput()` – text output
   - `plotOutput()` – Graphic output
3. **Server mode:**

   - `output$ID <- renderXXX({...})` – Create output
   - `input$ID` – Get input value
   - `observeEvent()` – Listen for events

### 8.2 Preview for tomorrow

Tomorrow we will learn:

- How to make the app structure clearer (layout and theme)
- More layout options
- Add CSS beautification

Congratulations!

You have successfully created your first Shiny App!
Remember: practice more and it’s normal to make mistakes.
Every mistake is a learning opportunity!

Homework

Try to make a "height and weight BMI calculator" based on what you learned today:

- Two sliders: height (cm) and weight (kg)
- Display calculated BMI value
- Display health advice based on BMI value

BMI = weight (kg) / (height (m) × height (m))
