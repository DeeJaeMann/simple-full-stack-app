# Code Platoon Full-Stack Immersive Program Landing Site

![Wiz](./sources/wiz.png)

## Scenario

Embark on an exhilarating journey as a junior developer tasked with creating the landing site for Code Platoon's Full-Stack Immersive Program after an unexpected crash! Picture this: you've been chosen as the hero to bring innovation and life to their digital presence. Code Platoon, recognizing your potential, has granted you unprecedented freedom to showcase your creativity and spontaneity in crafting the ultimate full-stack application.

Imagine yourself standing at the crossroads of technology, armed with the subjects that form the backbone of Code Platoon's Full-Stack Immersive Program and the profiles of the incredible instructors who guide aspiring developers on this adventure.

Your mission, should you choose to accept it, involves not just rebuilding a website but creating an immersive digital experience that captures the essence of Code Platoon's commitment to excellence in their Full-Stack Immersive Program. Unleash your coding superpowers and design a platform that not only informs but captivates potential students and celebrates the Code Platoon community.

## Requirements

### Database

- Create a PostgreSQL Database with the power to hold the knowledge gems, also known as the different subjects taught in Code Platoon's Full-Stack Immersive Program.
  - `subjects`: Your treasure chest for organizing the subjects in a way that ignites curiosity, sorted by difficulty from beginner-friendly to the advanced.

- Construct a sanctum for the mentors who guide future tech wizards.
  - `instructors`: A hall of fame showcasing the 10 instructors, each with a unique story, sorted not just by age but as beacons of wisdom from the most experienced to the young trailblazers.

### Flask Server

- Forge a Flask server, a beacon of connectivity, with two majestic portals:
  - `/api/v1/subjects/`: A magical gateway revealing an array of objects representing each subject in the full-stack immersive program, enchantingly sorted by difficulty to guide aspiring sorcerers on their learning journey. (Easiest to Hardest)

  ```json
  [{
    "description": "Markup language used for creating the structure of web pages.",
    "difficulty_level": 1,
    "id": 5,
    "title": "HTML"
  },
  {
    "description": "Scripting language commonly used for web development.",
    "difficulty_level": 2,
    "id": 2,
    "title": "Javascript"
  },
  {
    "description": "Style sheet language for enhancing the presentation of web pages.",
    "difficulty_level": 2,
    "id": 6,
    "title": "CSS"
  },
  {
    "description": "Lightweight web framework in Python for building web applications.",
    "difficulty_level": 2,
    "id": 10,
    "title": "Flask"
  },
  {
    "description": "Amazon's scalable and highly available Domain Name System (DNS) web service.",
    "difficulty_level": 2,
    "id": 13,
    "title": "Route53"
  },
  {
    "description": "High-level programming language known for its readability and versatility.",
    "difficulty_level": 3,
    "id": 1,
    "title": "Python"
  },
  {
    "description": "Study of organizing and storing data for efficient retrieval and manipulation.",
    "difficulty_level": 3,
    "id": 4,
    "title": "Data Structures"
  },
  {
    "description": "JavaScript library for building user interfaces particularly for single-page applications.",
    "difficulty_level": 3,
    "id": 7,
    "title": "React"
  },
  {
    "description": "Structured Query Language for managing and manipulating relational databases.",
    "difficulty_level": 3,
    "id": 8,
    "title": "SQL"
  },
  {
    "description": "Powerful open-source relational database management system.",
    "difficulty_level": 3,
    "id": 11,
    "title": "PostgreSQL"
  },
  {
    "description": "Object-Oriented Programming paradigm for structuring code.",
    "difficulty_level": 4,
    "id": 3,
    "title": "OOP"
  },
  {
    "description": "High-level Python web framework for rapid development and clean pragmatic design.",
    "difficulty_level": 4,
    "id": 9,
    "title": "Django"
  },
  {
    "description": "Elastic Compute Cloud for scalable and resizable compute capacity.",
    "difficulty_level": 4,
    "id": 12,
    "title": "AWS EC2"
  }]

  ```

  - `/api/v1/instructors/`: The mystical doorway leading to an array of objects representing each instructor, not just ordered by age, but crafted to unveil the wisdom in a chronological tapestry. (Sorted Oldest to Youngest)

  ```json
  [
  {
    "age": 45,
    "description": "Experienced professional in the enchanted realms of arts and literature education.",
    "id": 5,
    "name": "Robert Brown"
  },
  {
    "age": 40,
    "description": "Enthusiastic teacher with expertise in the ancient scrolls of mathematics.",
    "id": 3,
    "name": "Michael Johnson"
  },
  {
    "age": 38,
    "description": "Passionate about history and making it interesting for students weaving tales of the past like a magical bard.",
    "id": 7,
    "name": "David Taylor"
  },
  {
    "age": 36,
    "description": "Dynamic instructor with a focus on physical education shaping aspiring wizards for the challenges ahead.",
    "id": 9,
    "name": "Daniel White"
  },
  {
    "age": 35,
    "description": "Experienced instructor with a passion for teaching the magical arts of coding.",
    "id": 1,
    "name": "John Doe"
  },
  {
    "age": 32,
    "description": "Inspiring and dedicated instructor focusing on the mystical secrets of science education.",
    "id": 4,
    "name": "Emily Anderson"
  },
  {
    "age": 31,
    "description": "Innovative educator dedicated to fostering critical thinking skills guiding students like a wise wizard.",
    "id": 8,
    "name": "Sophia Clark"
  },
  {
    "age": 29,
    "description": "Energetic and creative instructor with a background in the melodic spells of music.",
    "id": 6,
    "name": "Olivia Miller"
  },
  {
    "age": 28,
    "description": "Friendly and knowledgeable educator specializing in the mystical world of technology.",
    "id": 2,
    "name": "Jane Smith"
  },
  {
    "age": 27,
    "description": "Focused on language arts and effective communication skills imparting the magical art of expression.",
    "id": 10,
    "name": "Ava Martin"
  }
  ]
  ```

### Front End Application

- Develop a Front-End masterpiece, a user interface that becomes a canvas for aspiring wizards to explore the magic of Code Platoon's Full-Stack Immersive Program.
  - Home Page: An inviting portal to the Code Platoon's Full-Stack Immersive Program, enticing visitors to embark on a magical coding adventure.
  - Subject Page: An interactive spellbook displaying each subject, waiting to be mastered by those brave enough to delve into the arcane arts.
  - Meet the Team Page: A gallery of mentors, each with a magical profile, showcased for students to connect with their future guides.
  - Sign-up Form: A magical scroll allowing potential apprentices to express their desire to join Code Platoon's full-time Immersive Program.
  - Utilize at least 1 3rd Party API: Summon the power of external APIs to adorn the pages with context-appropriate images, making the experience truly enchanting.
  