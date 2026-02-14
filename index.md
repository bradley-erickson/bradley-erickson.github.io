<style>
.inline-icon { height: 1em; width: auto; vertical-align: text-top; margin-top: 4px }
</style>

# Bradley Erickson

---

North Carolina


Software Engineer specializing in real-time data pipeline architecture, stream processing systems, and interactive analytics platforms. 5+ years building scalable Python backends and end-to-end data infrastructure.

## Professional Experience ![](/assets/building.svg){:.inline-icon}

---

### Technical Lead — Assistant Research Engineer 

Education Testing Service · Remote · Feb 2023 – Present

Served as principal engineer and architectural lead for the Learning Observer, an open-source, modular real-time data processing platform designed to make inferences from high-volume learning event streams. Originally joined the project during my MS at NC State, then transitioned to ETS to take over and expand its technical direction.

**Core Platform Architecture**

* Took ownership of and re-engineered the platform's core event processing pipeline into an async generator-based architecture built on reducer patterns, processing high-volume real-time student event streams into composable, queryable analytics  
* Designed and implemented a SQL-like query language enabling dashboards to declaratively compose real-time aggregations over reducer-based data stores  
* Built a pluggable frontend framework supporting dual dashboard architectures (Dash/Plotly and Next.js/React), allowing researchers to develop and deploy new analytics modules independently  
* Developed open-source Python frameworks for educational data collection and analysis, enabling external researchers to extend the platform without modifying core infrastructure

**Google Docs Writing Analytics Pipeline**

* Engineered a pipeline to capture and restream Google Docs AJAX change-set events in real-time, reconstructing full document state through reducer-based processing and feeding NLP/AI inference layers (classical NLP, BERT, LLMs) developed by ETS research scientists  
* Co-developed a JavaScript event capture library supporting multiple logging frameworks and event schemas for classroom deployment

**Deployment & Operations**

* Deployed platform as an LTI 1.3 application enabling single sign-on launches from Canvas, Schoology, and other LMS platforms across multiple school districts  
* Implemented CI/CD pipeline with GitHub Actions automating documentation builds, test execution, and deployments — reducing release cycles from days to hours  
* Collaborated directly with teachers across 4 schools, conducting workshops and iterating on design based on practitioner feedback from live classroom deployments  
* Led documentation initiative producing comprehensive API references and deployment guides  
* Mentored 3 graduate students on async Python patterns and system architecture

---

### Full Stack Engineer 

Trainer Hill LLC · Personal Venture · Dec 2020 – Present · [trainerhill.com](http://trainerhill.com)

Independently designed, built, and operate a competitive Pokémon TCG analytics platform end-to-end — from data acquisition through production infrastructure.

* Architected an automated ETL pipeline that scrapes, normalizes, and aggregates thousands of tournament results from heterogeneous sources into a unified analytical data model  
* Migrated from MongoDB to PostgreSQL to properly model complex relational data — deck compositions, matchup histories, tournament structures — significantly improving query performance  
* Implemented Redis caching layer reducing response times for high-traffic analytical endpoints  
* Built 12+ interactive analytical dashboards and tools using Dash and Plotly: deck performance metrics, meta-game trend analysis, card synergy identification, matchup predictions, and community-focused utilities  
* Developed a paid game-tracking service enabling competitive players to log, analyze, and improve their tournament performance  
* Managed production infrastructure on Digital Ocean: PostgreSQL optimization, Redis deployment, automated backups, SSL/CDN configuration, and zero-downtime deployments  
* Grew platform to 20,000+ monthly page views; monetized through paid services and advertising

---

### Software Engineer Intern

Digi International · Rochester, MN · May 2019 – Aug 2019

* Developed ReactJS features for an IoT device management portal in a Scrum environment

### Software Developer and Tester

Winona State University · Winona, MN · Nov 2017 – May 2020

* Developed and tested IoT management portal features as part of a university-industry partnership  
* Containerized application deployment pipeline using Docker  
* Prototyped low-energy Bluetooth device connectivity

## 

## Education ![](/assets/graduation-cap.svg){:.inline-icon}												   

---

**MS Computer Science** | North Carolina State University | 2022  
**BS Computer Science, BS Data Science, BA Mathematics** (Minor Statistics) | Winona State University | 2020

## 

## Skills ![](/assets/brain.svg){:.inline-icon}

---

Languages 		| Python, Javascript, Bash  
Web & API		| Flask, FastAPI, Asyncio, Dash, React, Next.js, RESTful APIs, WebSockets, LTI 1.3  
Data & Visualization 	| Pandas, NumPy, Plotly, Matplotlib, Shiny, Tableau  
Databases 		| PostgreSQL, MySQL, Redis / ValKey, MongoDB  
Infrastructure 		| GIT, Docker, Digital Ocean, Postman, Sphinx  
Testing & CI?CD 	| pytest, GitHub Actions

## Publications  ![](/assets/file.svg){:.inline-icon}

---

Mitros, P., Deane, P., Lynch, C., & **Erickson, B.** (2024, July). The Learning Observer: A Prototype System for the Integration of Learning Data. In *International Conference on Artificial Intelligence in Education* (pp. 432-438). Cham: Springer Nature Switzerland.

Gao, Z., **Erickson, B.**, Xu, Y., Lynch, C., Heckman, S., & Barnes, T. (2022). You Asked, Now What? Modeling Students' Help-Seeking and Coding Actions from Request to Resolution. *Journal of Educational Data Mining*, *14*(3), 109-131.

Gao, Z., **Erickson, B.**, Xu, Y., Lynch, C., Heckman, S., & Barnes, T. (2022). Admitting you have a problem is the first step: Modeling when and why students seek help in programming assignments. *International Educational Data Mining Society*.

**Erickson, B.**, Heckman, S., & Lynch, C. F. (2022, February). Characterizing Student Development Progress: Validating Student Adherence to Project Milestones. In Proceedings of the 53rd ACM Technical Symposium on Computer Science Education-Volume 1 (pp. 15-21).
