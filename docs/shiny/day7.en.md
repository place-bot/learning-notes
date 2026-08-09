# Day 7: Deploy and go live - let others access your app

## 1. Why deploy?

### 1.1 Current issues

The Shiny App you made can only be run on your own computer:

- Cannot be seen by others
- Can't share links
- Requires R environment to run

### 1.2 Benefits after deployment

After deployment, your app:

- Have independent website
- Anyone can access
- No need to install R

## 2. Preparation before deployment

### 2.1 Check your code

Before deploying, make sure there are no problems with the code:

```r
#Bad habit: use absolute paths
data <- read.csv("C:/Users/Zhang San/Desktop/data.csv")

#Good habit: use relative paths
data <- read.csv("data.csv")
```

### 2.2 Create item folder

Organize your file structure:

```text
my_app/
├── app.R # Shiny application code
├── data/ # data folder
│   └── data.csv
└── www/ # Static files (pictures, CSS, etc.)
    └── logo.png
```

### 2.3 Test dependency packages

List all packages you use:

```r
#List all packages at the beginning of app.R
library(shiny)
library(ggplot2)
library(DT)
#... Other packages
```

## 3. Method 1: shinyapps.io

### 3.1 What is shinyapps.io?

- Shiny App Hosting by Posit
- Suitable for personal items, teaching demonstrations and lightweight prototypes
- The free tier usually has restrictions on the number of applications, running time and resources, which are subject to the current instructions on the account page.

### 3.2 Register an account

1. Visit https://www.shinyapps.io/
2. Click "Sign Up"
3. Register with email (recommended to use GitHub account)

### 3.3 Install rsconnect package

```r
install.packages("rsconnect")
library(rsconnect)
```

### 3.4 Connect your account

On shinyapps.io:

1. After logging in, click your username
2. Select "Tokens"
3. Click "Show" to display the Token

Run the code shown in R:

```r
rsconnect::setAccountInfo(
  name='Your username',
  token='Your token',
  secret='Your secret'
)
```

### 3.5 Deploy application

The simplest deployment command:

```r
#Make sure it is under the Applications directory.
setwd("path/to/my_app")

#Deployment
rsconnect::deployApp()
```

### 3.6 Output during deployment

```text
Preparing to deploy application...
Uploading bundle for application: 1234567...
Deploying bundle: 1234567 for application: 1234567...
Building image: 1234567...
Starting instance...
Application successfully deployed to https://username.shinyapps.io/my_app/
```

After successful deployment, the console will output the public access address; this address is the online entrance to the application.

## 4. Handle deployment issues

### 4.1 The file is too large

If an error occurs:

```text
Error: The application is too large to be deployed.
```

Solution:

```r
#Check the size of the folder
#Free account limit 1GB

#Solution 1: Compress data
data <- read.csv("big_data.csv")
#Only keep the columns you need.
data_small <- data[, c("col1", "col2")]
write.csv(data_small, "data.csv")

#Solution 2: Use data sampling
data_sample <- data[sample(nrow(data), 1000), ]
```

### 4.2 Package issues

If a package fails to be installed on the server, priority is given to declaring dependencies in the item instead of installing the package when `app.R` is running:

```r
#Recommendation: Initialize renv locally and submit renv.lock
install.packages("renv")
renv::init()
renv::snapshot()
```

For small teaching items, you can also confirm that all dependent packages have been installed before deployment, and only keep the `library()` call on top of `app.R`.

### 4.3 Chinese display problem

```text
# Make sure the source file is saved in UTF-8
options(encoding = "UTF-8")

# Explicitly specify the encoding when reading the file
read.csv("data.csv", fileEncoding = "UTF-8")

# Specify available fonts when drawing
theme_set(theme_minimal(base_family = "sans"))
```

## 5. Manage deployed applications

### 5.1 View application list

```r
#View all deployed applications
rsconnect::applications()
```

### 5.2 Update application

Modify the code and redeploy:

```r
#It will automatically overwrite the original version.
rsconnect::deployApp()
```

### 5.3 Stop application

```r
#Temporarily stop the application.
rsconnect::terminateApp("my_app")
```

### 5.4 View application logs

On the shinyapps.io website:

1. Enter Dashboard
2. Click on your app
3. Select "Logs" to view the run logs

## 6. Method 2: Local network sharing

### 6.1 Applicable scenarios

- Only want to share at office/home
- Don't want to upload to the Internet
- Data is relatively sensitive

### 6.2 Obtain the local IP address

Windows:

```text
ipconfig
# Find the IPv4 address, such as 192.168.1.100
```

Mac/Linux:

```text
ifconfig
# Find the inet address
```

### 6.3 Modify the running mode

```text
# Don't use this
runApp()

# Change to this
runApp(host = "0.0.0.0", port = 5678)
```

### 6.4 Sharing address

Tell colleagues to visit:

```text
http://YOUR_IP_ADDRESS:5678
For example: http://192.168.1.100:5678
```

**Note:** Must be on the same network!

## 7. Method 3: Package into a stand-alone program

### 7.1 Use RInno to create an installation package

Install RInno:

```r
install.packages("RInno")
library(RInno)
```

### 7.2 Create an installer

```text
# Create installation configuration
create_app(
  app_name = "My data analysis tool",
  app_dir = "path/to/my_app",
  dir_out = "installer"
)

# Compile the installer
compile_iss()
```

### 7.3 Share exe files

The generated `.exe` file can:

- Send to others to install
- No R environment required
- Use like normal software

## 8. Optimize deployed applications

### 8.1 Add loading animation

```r
#UI end
ui <- fluidPage(
  #Add loading prompts
  tags$head(
    tags$style(
      ".shiny-busy {
        position: fixed;
        top: 50%;
        left: 50%;
        margin-top: -25px;
        margin-left: -50px;
        background-color: #000;
        color: white;
        padding: 10px;
        border-radius: 5px;
      }"
    )
  ),

  #Other UI elements...
)
```

### 8.2 Optimize startup speed

```r
#Put data reading outside the app.
#This way, it is read only once, not by every user.

#Global data (beginning with app.R)
global_data <- read.csv("data.csv")

ui <- fluidPage(...)

server <- function(input, output) {
  #Use global data
  data <- reactive({
    global_data
  })
}
```

### 8.3 Limit file upload size

```text
# Set the maximum upload size to 10MB
options(shiny.maxRequestSize = 10*1024^2)
```

## 9. Practice: Deploying our data exploration tools

### 9.1 Prepare files

Create folder structure:

```text
data_explorer/
├── app.R
├── sample_data.csv # Sample data
└── README.md # Documentation
```

### 9.2 Add sample data

```r
#Add in app.R
ui <- fluidPage(
  #... Other codes

  #Add example data button
  actionButton("use_sample", "Use example data"),

  #... Other codes
)

server <- function(input, output) {
  #Response example data button
  observeEvent(input$use_sample, {
    #Use the built-in dataset
    values$data <- iris

    showNotification(
      "Sample data has been loaded: Iris dataset",
      type = "success"
    )
  })

  #... Other codes
}
```

### 9.3 Add usage instructions

```r
ui <- fluidPage(
  titlePanel("Data exploration tool"),

  #Addition instructions
  tags$div(
    class = "well",
    h4("Instructions for use"),
    tags$ol(
      tags$li("Click 'Use sample data' to experience it quickly"),
      tags$li("Or upload your own CSV file."),
      tags$li("Select the numerical column to be analyzed."),
      tags$li("View statistical charts and summaries")
    )
  ),

  #... Other codes
)
```

### 9.4 Deployment command

```r
#Set the application name
rsconnect::deployApp(
  appName = "data-explorer",
  appTitle = "Data exploration tool"
)
```

## 10. Post-deployment maintenance

### 10.1 Monitor usage

You can see this in the shinyapps.io console:

- Number of visits
- Duration of use
- Error log

### 10.2 Set access restrictions

The following examples are suitable for educational demonstration only. For real items, do not write the password into the source code; use shinyapps.io account permissions, reverse proxy authentication, corporate identity authentication, or at least read the key through environment variables.

```r
#Teaching example: Using environment variables to provide demonstration passwords
ui <- fluidPage(
  #Login interface
  conditionalPanel(
    condition = "!output.authenticated",
    wellPanel(
      h3("Please log in."),
      passwordInput("password", "Password:"),
      actionButton("login", "enter")
    )
  ),

  #Main interface
  conditionalPanel(
    condition = "output.authenticated",
    #Your application content
  )
)

server <- function(input, output, session) {
  #Certification status
  authenticated <- reactiveVal(FALSE)

  #Login logic
  observeEvent(input$login, {
    if (identical(input$password, Sys.getenv("APP_PASSWORD"))) {
      authenticated(TRUE)
    } else {
      showNotification("Wrong password", type = "error")
    }
  })

  #Output certification status
  output$authenticated <- reactive({
    authenticated()
  })
  outputOptions(output, "authenticated",
                suspendWhenHidden = FALSE)
}
```

### 10.3 Add Google Analytics

If your app handles personal or classroom data, you should confirm the privacy notice and institutional requirements before including statistics scripts.

```text
#Add in the head of the UI
tags$head(
  tags$script(
    src = "https://www.googletagmanager.com/gtag/js?id=YOUR_ID"
  ),
  tags$script(
    HTML("
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'YOUR_ID');
    ")
  )
)
```

## 11. Comparison of different deployment methods

### 11.1 Method comparison table

|way|Advantages|Disadvantages|Applicable scenarios|
| --- | --- | --- | --- |
| shinyapps.io |Simple and fast|There is a time limit|Personal items and demonstrations|
|local network|Data security|Can only be accessed via intranet|Office sharing|
|package exe|like software|The file is larger|Distribute to customers|
|Self-built server|full control|Need technology|Enterprise applications|

### 11.2 Select recommendations

**If you are a beginner:**
→ Use shinyapps.io

**If you are using within your company:**
→ Local network sharing

**If you want to use it for customers:**
→Package into exe

**If you are a professional developer:**
→ Consider building your own server

## 12. Frequently Asked Questions and Answers

### 12.1 Deployment failed

```text
Error: HTTP 413
Request entity too large
```

Solution: Reduce file size

### 12.2 Application is slow

Cause and solution:

1. **Data is too big** → Use data sampling
2. **Complex calculation** → Use reactive cache
3. **Too many packages** → only load necessary packages

### 12.3 Chinese garbled characters

```text
# Make sure scripts and data files are saved as UTF-8
options(encoding = "UTF-8")

# Explicitly specify encoding when reading external files
read.csv("data.csv", fileEncoding = "UTF-8")
```

`Sys.setlocale("LC_ALL", "C")` is not recommended for solving Chinese problems; the `C` locale generally makes non-ASCII text processing more limited.

## 13. Deployment Checklist

Pre-deployment checks:

- The code runs fine locally
- No absolute paths used
- Data files are in the correct location
- All packages are declared
- The total file size is reasonable
- Added error handling
- Has basic instructions for use
- Tested on different browsers

## 14. Advanced: Automated deployment

### 14.1 Using GitHub Actions

Create `.github/workflows/deploy.yml`:

```r
name: Deploy to shinyapps.io

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    env:
      SHINY_NAME: ${{ secrets.SHINY_NAME }}
      SHINY_TOKEN: ${{ secrets.SHINY_TOKEN }}
      SHINY_SECRET: ${{ secrets.SHINY_SECRET }}
    steps:
    - uses: actions/checkout@v6

    - uses: r-lib/actions/setup-r@v2

    - name: Install packages
      run: |
        Rscript -e 'install.packages(c("rsconnect", "renv"), repos = "https://cloud.r-project.org")'
        Rscript -e 'renv::restore(prompt = FALSE)'

    - name: Deploy
      run: |
        Rscript -e 'rsconnect::setAccountInfo(name = Sys.getenv("SHINY_NAME"), token = Sys.getenv("SHINY_TOKEN"), secret = Sys.getenv("SHINY_SECRET")); rsconnect::deployApp()'
```

### 14.2 Benefits

- Push code to automatically deploy
- No need to run commands manually
- Place deployment credentials in GitHub Secrets to avoid writing into the source code

## 15. Summary and Outlook

### 15.1 You learned

1. **Three deployment methods**:

   - Cloud deployment (shinyapps.io)
   - Local sharing
   - Package and distribute
2. **Deployment Tips**:

   - Optimize performance
   - Handle errors
   - Added features
3. **Maintenance Method**:

   - Monitor usage
   - updated version
   - Collect feedback

### 15.2 Next step

1. **Improving the application**:

   - Add more features
   - Improve user experience
   - Optimize performance
2. **Learning Advanced**:

   - Shiny Server self-built
   - Docker containerization
   - Load balancing
3. **Create a portfolio**:

   - GitHub show code
   - Personal website display application
   - Write a blog to share experiences

## 16. Weekly study summary

### 16.1 Review of learning paths

```text
Day 1: Hello World → Basic interaction
Day 2: Layout beautification → Professional interface
Day 3: Input controls → User interaction
Day 4: Display result → data output
Day 5: Reactive Programming → Core Concepts
Day 6: Practical items → Comprehensive application
Day 7: Deployment and online → Share results
```

### 16.2 Core Skills List

**Basic Skills:**

- ✓ Create UI and Server
- ✓ Use various inputs and outputs
- ✓ Master layout methods
- ✓ Understand reactive programming

**Advanced skills:**

- ✓ Dynamic UI generation
- ✓ File upload and download
- ✓ Error handling
- ✓ Deployment and release

### 16.3 Continue learning resources

**Official Source:**

- [Shiny official website](https://shiny.posit.co/)
- [Shiny Gallery](https://shiny.posit.co/r/gallery/)
- [Mastering Shiny](https://mastering-shiny.org/)

**Community Resources:**

- [Posit Community](https://community.rstudio.com/c/shiny)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/shiny)
- [GitHub excellent item](https://github.com/topics/shiny)

**Video Tutorial:**

- YouTube: "Shiny Tutorial"
- Coursera: "Developing Data Products"
- DataCamp: "Building Web Applications with Shiny"

### 16.4 Final words

After completing the 7-day learning path, it is recommended to continue to consolidate through real data items.

From Hello World on the first day to being able to deploy your own applications today, you have mastered the core skills of Shiny development.

The example can be expanded into a reusable data analysis application in the future.
