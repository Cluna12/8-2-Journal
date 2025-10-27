# 8-2-Journal

---- How do you write programs that are maintainable, readable, and adaptable?
I write programs that are maintainable by organizing code into logical modules and using clear function and variable names. In this project, I created a separate CRUD Python module to handle all database interactions. This made the dashboard code cleaner and easier to manage because database logic was not mixed in with dashboard display code. The CRUD module also made the program adaptable—if the database changes in the future, I would only need to update one file. This module could also be reused in another application, such as a REST API or a mobile app that needs access to the same MongoDB collection.

---- How do you approach a problem as a computer scientist?
I approach problems by breaking them down into smaller, manageable tasks. In this project, I first made sure I could connect to the MongoDB database and retrieve data. Then I built the dashboard step by step: table first, filters next, and visualizations last. I tested each component as I added it, which made it easier to find and fix issues early. This approach was more complex than earlier assignments because it combined database design, backend logic, and frontend interaction. In future projects, I would continue using this modular problem-solving strategy, especially when working with real client requirements and data.

---- What do computer scientists do, and why does it matter?
Computer scientists solve real-world problems using technology. In this project, I built a dashboard that helps Grazioso Salvare quickly find dogs suitable for search and rescue training. This shows how data and software can support meaningful decision making. Work like this matters because companies rely on accurate data tools to make faster, smarter choices. As a computer scientist, creating tools that organize data, improve workflow, and solve business problems adds real value to organizations.
