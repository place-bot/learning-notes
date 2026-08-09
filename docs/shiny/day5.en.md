# Day 5: Fundamentals of reactive programming - the core thinking of Shiny

## 1. Understand the thinking of reactive programming

### 1.1 What is a reaction?

Imagine a simple scenario:

```text
Thermometer shows temperature
Temperature changes → display automatically updates
```

This is the core of reactivity: **automatic updates**.

### 1.2 Experience reactivity in Shiny

Let’s look at the simplest example first:

```r
library(shiny)

ui <- fluidPage(
  sliderInput("x", "Select the number:", 1, 10, 5),
  textOutput("y")
)

server <- function(input, output) {
  output$y <- renderText({
    paste("You chose:", input$x)
  })
}

shinyApp(ui, server)
```

**Key points of thinking:**

- The slider changes → the text automatically changes
- We didn't write any "listening" code
- Shiny handles it automatically

## 2. Why is reactive() needed?

### 2.1 Let’s look at a question first

Suppose we want to display the square and cube of a number:

```r
server <- function(input, output) {
  output$square <- renderText({
    input$x ^ 2
  })

  output$cube <- renderText({
    input$x ^ 3
  })
}
```

It's okay to write like this, but what if the calculation is complicated?

### 2.2 Problems with complex calculations

```r
server <- function(input, output) {
  output$result1 <- renderText({
    #Suppose this is a time-consuming calculation.
    Sys.sleep(2)  #Simulated time
    input$x * 100
  })

  output$result2 <- renderText({
    #Count it again!
    Sys.sleep(2)  #It takes time again.
    input$x * 100
  })
}
```

**Question:** The same calculation was done twice!

### 2.3 reactive() solution

```r
server <- function(input, output) {
  #Calculate once and save it.
  result <- reactive({
    Sys.sleep(2)  #It only takes one time.
    input$x * 100
  })

  output$result1 <- renderText({
    result()  #Pay attention to the parentheses!
  })

  output$result2 <- renderText({
    result()  #Reuse results
  })
}
```

**Thinking Points:**

- `reactive()` = Smart Cache
- Calculate once and use it many times
- Automatically recalculates when input changes

## 3. Reactive() way of thinking

### 3.1 Step 1: Identify duplicates

Look at this example:

```r
#Both charts need random data.
output$hist <- renderPlot({
  data <- rnorm(input$n)  #Generate data
  hist(data)
})

output$boxplot <- renderPlot({
  data <- rnorm(input$n)  #And different data are generated again!
  boxplot(data)
})
```

### 3.2 Step 2: Extract common parts

```r
#Bring up the commonalities
myData <- reactive({
  rnorm(input$n)
})
```

### 3.3 Step 3: Replacement

```r
output$hist <- renderPlot({
  hist(myData())  #Using the same data
})

output$boxplot <- renderPlot({
  boxplot(myData())  #Using the same data
})
```

### 3.4 Complete thinking process

```r
library(shiny)

ui <- fluidPage(
  sliderInput("n", "Data volume:", 10, 100, 50),
  plotOutput("hist"),
  plotOutput("box")
)

server <- function(input, output) {
  #Thinking 1: Data is generated only once.
  myData <- reactive({
    rnorm(input$n)
  })

  #Thinking 2: Use in multiple places
  output$hist <- renderPlot({
    hist(myData(), col = "lightblue")
  })

  output$box <- renderPlot({
    boxplot(myData(), col = "lightgreen")
  })
}

shinyApp(ui, server)
```

## 4. The way of thinking of observe()

### 4.1 The difference between reactive vs observe

```r
#reactive: calculated value
calculated <- reactive({
  input$x * 2  #Return a value
})

#observe: take action
observe({
  print(input$x)  #Perform an action
})
```

**Thinking difference:**

- `reactive`: What do I want to figure out?
- `observe`: What do I want to do?

### 4.2 When to use observe?

When you want "side effects":

```r
server <- function(input, output) {
  observe({
    #Print log (side effects)
    cat("The user chose:", input$choice, "\n")
  })
}
```

### 4.3 Practical Example: Debugging Assistant

```r
library(shiny)

ui <- fluidPage(
  textInput("name", "Name:"),
  sliderInput("age", "Age:", 1, 100, 25)
)

server <- function(input, output) {
  #Monitor all inputs with observe
  observe({
    cat("=== Input change ===\n")
    cat("Name:", input$name, "\n")
    cat("Age:", input$age, "\n\n")
  })
}

shinyApp(ui, server)
```

After running, look at the console and it will print every time you change the input!

## 5. The way of thinking of observeEvent()

### 5.1 Execute only at specific times

`observe()` is too sensitive and will be executed on any relevant input changes.
`observeEvent()` will only be executed at the time you specify.

```text
# observe: executed if name or age changes
observe({
  cat(input$name, input$age)
})

# observeEvent: only executed when the button is clicked
observeEvent(input$button, {
  cat(input$name, input$age)
})
```

### 5.2 Typical usage: button event

```r
library(shiny)

ui <- fluidPage(
  textInput("text", "Enter text:"),
  actionButton("save", "preserve")
)

server <- function(input, output) {
  observeEvent(input$save, {
    cat("Saved:", input$text, "\n")
  })
}

shinyApp(ui, server)
```

## 6. ReactiveValues() way of thinking

### 6.1 Why do we need to store variables?

In Shiny, normal variables do not trigger updates:

```r
#This can't be!
server <- function(input, output) {
  count <- 0  #Ordinary variables

  observeEvent(input$add, {
    count <- count + 1  #It has been modified, but the interface will not be updated.
  })
}
```

### 6.2 Using reactiveValues

```r
server <- function(input, output) {
  #Create a reactive variable
  values <- reactiveValues(count = 0)

  observeEvent(input$add, {
    values$count <- values$count + 1  #In this way, the interface will be updated!
  })
}
```

### 6.3 Simple counter

```r
library(shiny)

ui <- fluidPage(
  actionButton("add", "+1"),
  actionButton("minus", "-1"),
  h3(textOutput("count"))
)

server <- function(input, output) {
  #Storage count
  values <- reactiveValues(count = 0)

  #Add
  observeEvent(input$add, {
    values$count <- values$count + 1
  })

  #reduce
  observeEvent(input$minus, {
    values$count <- values$count - 1
  })

  #Display
  output$count <- renderText(values$count)
}

shinyApp(ui, server)
```

## 7. Building complex functions

### 7.1 Thinking steps

1. **Input** → What can the user change?
2. **Status** → What to remember? (reactiveValues)
3. **Calculation** → What needs to be calculated? (reactive)
4. **Action** → What needs to be done? (observeEvent)
5. **Output** → What is displayed? (renderXXX)

### 7.2 Example: Simple Shopping Cart

**Step 1: Analyze requirements**

```text
# Requirements:
# 1. Users can select products from the drop-down menu
# 2. Click the button to add items to the shopping cart
# 3. Display the list and total price of the selected products in the shopping cart
# 4. Provide a "clear shopping cart" button
```

**Step 2: Design Status**

```r
#Use reactiveValues to save the status of the shopping cart.
#Here we record the product name and price at the same time.
values <- reactiveValues(
  cart = character(0),   #Store the product code (e.g., "apple")
  prices = numeric(0)    #Store the corresponding price.
)
```

> Explanation: Although the actual code can only store the product name and look up the table to obtain the price, here for the sake of clarity of teaching, the method of explicitly recording the price is retained, so that the data structure corresponds one to one for easy observation.

**Step 3: Add input**

```r
ui <- fluidPage(
  selectInput("item", "Select products:",
              choices = c("Apple-5 yuan" = "apple",
                          "Banana-3 yuan" = "banana",
                          "Orange-4 yuan" = "orange")),
  actionButton("add", "Add to shopping cart")
)
```

> Explanation: Use `selectInput()` to create a drop-down box to display the product and price; after the user selects it, click `actionButton()` to add the product.

**Step 4: Processing Actions**

```r
#Product price search table
price_table <- c(apple = 5, banana = 3, orange = 4)

#Add product logic
observeEvent(input$add, {
  #Add the product name to the shopping cart.
  values$cart <- c(values$cart, input$item)

  #Find the price from the price list and add it.
  values$prices <- c(values$prices, price_table[input$item])
})
```

> Explanation: `observeEvent` is triggered when the button is clicked, reads the item from the input, and updates `cart` and `prices`.

**Step 5: Calculate the total price**

```r
#Calculate the total price in real time
total <- reactive({
  sum(values$prices)
})
```

> Explanation: Whenever the price in the shopping cart changes, the total price is automatically updated.

**Step Six: Complete Combination**

```r
library(shiny)

ui <- fluidPage(
  h3("Simple shopping cart"),

  #Product selection input
  selectInput("item", "Select products:",
              choices = c("Apple-5 yuan" = "apple",
                          "Banana-3 yuan" = "banana",
                          "Orange-4 yuan" = "orange")),
  actionButton("add", "add"),
  actionButton("clear", "Clear"),

  hr(),

  #Show the contents of the shopping cart
  h4("Shopping cart:"),
  verbatimTextOutput("cart"),

  #Show the total price
  h4(textOutput("total"))
)

server <- function(input, output) {
  #Product Price List (for lookup)
  prices <- c(apple = 5, banana = 3, orange = 4)
  #Product name mapping (for display)
  names_cn <- c(apple = "Apple", banana = "banana", orange = "orange")

  #Status record: product code and price
  values <- reactiveValues(
    cart = character(0),
    prices = numeric(0)
  )

  #Add products to the shopping cart
  observeEvent(input$add, {
    values$cart <- c(values$cart, input$item)
    values$prices <- c(values$prices, prices[input$item])
  })

  #Empty the shopping cart
  observeEvent(input$clear, {
    values$cart <- character(0)
    values$prices <- numeric(0)
  })

  #Calculate the total price in real time
  total <- reactive({
    sum(values$prices)
  })

  #Show the contents of the shopping cart
  output$cart <- renderPrint({
    if (length(values$cart) == 0) {
      "The shopping cart is empty."
    } else {
      #Display the Chinese name and quantity of the product.
      table(names_cn[values$cart])
    }
  })

  #Show the total price
  output$total <- renderText({
    paste("Total price:", total(), "Yuan")
  })
}

shinyApp(ui, server)
```

## 8. The thinking model of reactive programming

### 8.1 Three Thinking Modes

1. **Transfer of value** (reactive)

```text
A changes → B automatically recalculates → C automatically updates
```

1. **Event response** (observeEvent)

```text
Button click → perform specific action
```

1. **State Management** (reactiveValues)

```text
Store mutable state → state change → interface update
```

### 8.2 Selection Guide

Ask yourself these questions:

- What should I **calculate**? → `reactive()`
- What am I going to do? → `observeEvent()`
- What should I **remember**? → `reactiveValues()`
- What should I **keep monitoring**? → `observe()`

### 8.3 Common patterns

**Mode 1: Input Processing**

```r
#Process user input
cleaned_input <- reactive({
  #Clean, validate, and convert inputs
  toupper(input$text)
})
```

**Mode 2: Data Pipeline**

```r
#Original data
raw_data <- reactive({
  read.csv(input$file$datapath)
})

#Clean up data
clean_data <- reactive({
  na.omit(raw_data())
})

#Analysis results
results <- reactive({
  summary(clean_data())
})
```

**Mode 3: User Interaction**

```r
#Status
values <- reactiveValues(step = 1)

#The next step
observeEvent(input$next, {
  values$step <- values$step + 1
})

#The previous step
observeEvent(input$prev, {
  values$step <- values$step - 1
})
```

## 9. Debugging reactive code

### 9.1 Using browser()

```r
my_reactive <- reactive({
  browser()  #Pause here.
  input$x * 2
})
```

### 9.2 Print intermediate values

```r
my_reactive <- reactive({
  cat("The input value is:", input$x, "\n")
  result <- input$x * 2
  cat("The result is:", result, "\n")
  result
})
```

### 9.3 Use req() to avoid errors

```r
my_reactive <- reactive({
  req(input$file)  #Ensure that the document has been uploaded.
  read.csv(input$file$datapath)
})
```

## 10. Today’s summary

### 10.1 Core thinking

Reactive programming is to establish an automatic update chain:

```text
Input changes → Automatically trigger calculations → Automatically update display
```

### 10.2 Four core tools

1. **reactive()**: Create smart variables and automatically recalculate
2. **observe()**: Continuously monitor and perform side effects
3. **observeEvent()**: Triggered by a specific event
4. **reactiveValues()**: Store mutable state

### 10.3 Thinking process

1. Identify input (input)
2. Design status (reactiveValues)
3. Define calculation (reactive)
4. Handle events (observeEvent)
5. Generate output (render)

Congratulations on mastering reactive thinking!

The key to reactive programming is not to memorize functions, but to understand the way of thinking.
The more you practice, the more intuitive you will become.

Practice suggestions

Don't write complex applications right from the start. Start with a small function:

1. A button changes a number
2. Calculate one result from two inputs
3. Save the user’s selection history

Every small function is practicing reactive thinking!
