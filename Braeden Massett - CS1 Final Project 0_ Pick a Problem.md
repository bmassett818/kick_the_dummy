# Final Project: Pick a Project

## Computer Science \- Week 10 Oct 3, 2026 \- Version 0.0.2

Please make sure to your UD **email** AND **name** is below. Unless your UD emails are included in this table, then you will not earn any points for this assignment when it is graded\! **Every person should submit their own individual worksheet**.

Talk about each of the questions with a friend or [our LLM](https://chatgpt.com/g/g-6a6276313a9c8191af1f065698f516bf-drafter-planning-tool-v2-0-0b1) (or both), but **make sure the words you enter below are yours** (with the obvious exceptions notwithstanding). Brainstorming is best done in full sentences, and the main goal here is brainstorming. It's worth reviewing the information in [this series of pages in the Drafter documentation](https://drafter-edu.github.io/drafter/your-project/) to gain a better understanding of the process.

| Role | Name | Email |
| :---- | :---- | :---- |
| **Developer (You)** | Braeden Massett | bmassett@udel.edu |
| **Friend (optional)** | Nathaniel White | newhite@udel.edu |

# Part 1: The Goal & Prior Implementations

1. **Identify the Goal:** What specific goal are you trying to address? Think about your passions, hobbies, and academic interests. The latter are an excellent candidate to focus on. Some majors have suggestions listed below: these were provided by faculty in those departments. Other majors could consider a focus tied to a big final assignment in one of their recent courses in their major.   
   * **Biomedical Engineering** majors may consider one of the following:   
     * If you have started (or completed) the Cell/Tissue Design final project in BMEG100, design an organoid, which involves combining a cell type, biomaterial, and testing method. Have the website include a description and diagram of your design concept, a testing method, a needs statement, and an impact statement relevant to their organoid. Also include a link to a paper that supports your idea and a paragraph describing how that paper supports your design concept.  
     * Otherwise, create a website related to your BMEG100 Lab Report 1, *Cytoskeletal and Nuclear Staining Lab Report Guidelines*, linked [here](https://drive.google.com/file/d/1HCVznbmAN7tUk7J6VhhoowOoq4Rd7bdi/view?usp=sharing) (University of Delaware account required to access).  
   * **Chemistry** and **Chemical Engineering** majors may consider creating an automated chemistry assistant that takes balanced reaction equations, starting reactant masses, and a harvested product amount to determine the limiting reactant, theoretical yield, and percent yield based on principles from [Chemistry 2e (OpenStax) — Chapter 4: Chemical Reactions and Stoichiometry](https://chem.libretexts.org/Bookshelves/General_Chemistry/Chemistry_2e_\(OpenStax\)). To avoid manually compiling atomic mass tables or writing custom string tokenizers, use the [ChemPy](https://github.com/bjodah/chempy) library to parse molecular formulas into exact molecular weights and verify reaction stoichiometry against compound data from the [NIH PubChem Database](https://pubchem.ncbi.nlm.nih.gov/). The program outputs an organized breakdown of limiting reagent status, product yields, and remaining masses of unreacted species. Also use the heat of the reaction to determine if it is exothermic or endothermic, and compute the heat flow per mole of the product.  
   * Majors in the **Electric & Computer Engineering** department may consider a [steganography](https://en.wikipedia.org/wiki/Steganography) project that hides messages in images, and then retrieves those messages from uploaded images.   
   * **Mechanical Engineering** majors may consider a project that somehow uses both the [NumPy](https://en.wikipedia.org/wiki/NumPy) and [SciPy](https://en.wikipedia.org/wiki/SciPy) Python libraries. 

| *I was thinking of a way to better take notes electronically.* |
| :---- |

2. **Prior Implementations:** Search the internet. What existing tools or websites currently attempt to address it?

| *There are a good amount of notetaking tools that use AI to better summarize notes.* |
| :---- |

3. **Your Implementation:** Briefly describe the legitimate purpose or functionality of your site. How would you want this web application to be used?

| *The purpose of my web application would be to make the process of writing electronic notes easier and better organized. I would want this web application to be used during lectures to take notes.* |
| :---- |

# Part 2: The Input-Process-Output (IPO) Model

Think about the fundamental flow of your program.

1. **The Core Goal:** Every program has three main phases: taking input, processing data, and presenting output. In one sentence, what is the ultimate goal your program will accomplish for the user? Be specific and use CS1 concepts.

| This program will take in a string input from the user and return a page with the string from the user. The program should also be able to organize the pages and allow the user to increase the number of pages. |
| :---- |

2. Input: What specific information will the user need to provide to your program? (e.g., a city name, a numerical budget, a list of hobbies).

| The user will need to input page names and notes.  |
| :---- |

3. Processing: At a high level, how will the computer manipulate or evaluate that data? (e.g., calculate the average, filter out options that are too expensive, compare the input against a database).

| The computer might manipulate how the strings are shown on the page based on input from the user. |
| :---- |

4. Output: What will the user get back? (e.g., a recommendation, a calculated safety factor, a formatted schedule).

| The user will get back a properly formatted notebook page that shows all of their notes. |
| :---- |

# Part 3: Data Abstraction

Identify the "nouns" of your problem.

1. **Representing Reality:** Abstraction is the process of representing the real world inside a computer by ignoring unnecessary details. What are the core "things" (nouns) your program needs to track? (e.g., *If building a recipe app, the nouns are "Recipe" and "Ingredient"*).

| *Notebook Pages, Class Courses, Units, Headers, Text Properties* |
| :---- |

2. **Identifying Properties:** For the most important "thing" you listed above, what 3 to 4 specific details do you actually need to solve your problem, and what details will you [abstract](https://en.wikipedia.org/wiki/Abstraction_%28computer_science%29) away?  
   * *Details I need:* (e.g., *Ingredient name, weight, cost*)  
   * *Details I will ignore:* (e.g., *Ingredient color, brand, expiration date*)

| *I need the notebook page, the class course, the unit, and whether or not the string will be a header.* |
| :---- |

# Part 4: Challenges, AI Strategy, & Goals

1. **Difficulties:** What parts of this project seem the most difficult or technically complex?

| *The creation of new pages for each course and/or unit seems to be the most difficult.* |
| :---- |

2. **Coding Strategy:** If you will be using an LLM to help code, how will you ensure you understand the generated code and avoid "hallucinations" or "shallow learning" (copying without understanding)? If you won't be using an LLM to help code, this project might take about 4 hours a week to complete, so list each of the days and times in which you work on the project. 

| *I don’t plan on using an LLM to help me so I will work Tuesdays from 10:30-12:00 and Thursdays from 9:30-12:00.* |
| :---- |

3. **Goals:** What is your ultimate goal for this project? (e.g., *Impress the graders with a creative UI, build something I can use in my other classes, learn Drafter deeply*).

| *My ultimate goal for this project is to make a writing UI that is better for taking notes.* |
| :---- |

# Part 5: Research & Brainstorming Conversation

Have a conversation with a Generative AI tool (like ChatGPT or Claude) OR a friend about your project idea. Do not ask for code. Instead, use the AI/friend as a sounding board to research your problem.

1. **The Initial Prompt/Question:** Ask the AI or your friend to help you brainstorm. (e.g., *"I want to build a simple web tool to help students track their study hours. What are 3 common problems students face when tracking their time, and what are 3 simple features a basic tool should have?"*). Paste your prompt below:

| *I want to build a program that could help others take notes electronically, are there any web sites you know of that help do this. If so, what do they do right and what do they do wrong?* |
| :---- |

2. **The Response:** Briefly summarize the best ideas the AI or your friend suggested. What existing solutions or prior apps did they mention?

| *My friend suggested that he does not really use any electronic note taking apps during class, he does however use a web site that scans his written notes and uploads them for later.* |
| :---- |

3. **The Pushback:** You must reply to the AI/friend to narrow the scope when it's over-ambitious. Pick the most complex feature they suggested and explain why it is too complicated for an  introductory programming project. Ask them for a simpler alternative. *Paste your response here:*

| *I do not know how to create a way to scan papers using the coding that I know now. There is no input or anything I know that could accomplish that. Is there anything else you would want from an electronic note taking app?* |
| :---- |

4. **Reflection:** Based on this conversation, how has your project idea changed or become more focused?

| *I realized that I would not be able to create an electronic note taking app that would have features that would make it worthwhile. Also I was having difficulty figuring out how this program would complete the requirements for this project, so I decided I will be making a simple physics simulator.* |
| :---- |

# Part 6: Resource Planning

1. What resources will you use if you get stuck? 

| *I will ask a TA, the professor, or an LLM for help if I get stuck. I can also talk to people I know who can code if I get stuck.* |
| :---- |

2. If your LLM provides code that causes a Drafter or Bakery error, or if you run into a problem during deployment, what is your step-by-step debugging plan to resolve it?

| *I would read the error message first to see if it could give hints to what went wrong. If that does not help, I would read the code and say what each line is supposed to do aloud to make sure I did not miss anything, and if that does not work, I would ask for help from a TA, the professor, or an LLM.* |
| :---- |

# Part 7: LLM Conversation

If you used an LLM in any part of this work, copy and paste every part of that conversation below. Otherwise, you may be given a zero for the assignment. Obviously, these words will not all be yours, and this is the exception to the requirement at the top of this assignment that all responses be in your own words. If you did not use an LLM to assist you in this assignment, simply say so below.

| *I did not use an LLM to assist me in this assignment.* |
| :---- |

# Part 8: Submit

In Google docs, with this document open, please click on *File* \> *Download* \> *Microsoft Word (.docx)*, and make sure you put that download somewhere you can find it again. Then, upload it to the Canvas assignment about selecting or brainstorming your final project. 

When you're done with this assignment, review [this page of the Drafter documentation](https://drafter-edu.github.io/drafter/your-project/sketch-the-pages/) to better prepare for the next step.