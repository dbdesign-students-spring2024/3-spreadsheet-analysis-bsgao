# Spreadsheet Analysis

A little assignment to practice finding data, munging it, and analyzing it in a spreadsheet program.

Replace the contents of this file with a report, as described in the [instructions](./instructions.md).

### The Orignial Data

### Origin: NYC Open Data

### Name: 2019 DOE High School

### link: https://data.cityofnewyork.us/Education/2019-DOE-High-School-Directory/uq7m-95z8/about_data

### Format: csv

|----------|----------|----------|

### Simplified Table

Since there are 20 columns, I will only show the first four columns, since the raw data is extremely lengthy, and it was fairly difficult for me to import all 20 columns.

| dbn    | School Name                                       | Boro | Overview Paragraph                                         |
| ------ | ------------------------------------------------- | ---- | ---------------------------------------------------------- |
| 16K498 | Brooklyn High School for Law and Technology       | K    | The mission of Brooklyn High School for Law and...         |
| 17K524 | International High School at Prospect Heights     | K    | We are a small school that works in teams to p...          |
| 02M531 | Repertory Company High School for Theatre Arts    | M    | We offer a college-preparatory program and New...          |
| 05M670 | Thurgood Marshall Academy for Learning and Soc... | M    | Thurgood Marshall Academy is an academically r...          |
| 15K423 | Brooklyn Frontiers High School                    | K    | Brooklyn Frontiers High School serves entering...          |
| 03M291 | West End Secondary School                         | M    | We promote and support scholarly endeavors thr...          |
| 24Q299 | Bard High School Early College Queens             | Q    | Bard High School Early College Queens <<Output Truncated>> |
| 17K408 | Academy of Hospitality and Tourism                | K    | <<Output Truncated>>                                       |
| 19K683 | School for Classics High School                   | K    | <<Output Truncated>>                                       |
| 02M407 | Institute for Collaborative Education (ICE)       | M    | <<Output Truncated>>                                       |
| 27Q302 | Queens High School for Information, Research, ... | Q    | <<Output Truncated>>                                       |
| 12X251 | Explorations Academy                              | X    | <<Output Truncated>>                                       |
| 03M485 | Fiorello H. LaGuardia High School of Music & A... | M    | <<Output Truncated>>                                       |
| 15K429 | Digital Arts and Cinema Technology High School    | K    | <<Output Truncated>>                                       |
| 22K630 | Professional Pathways High School                 | K    | <<Output Truncated>>                                       |
| 21K559 | Life Academy High School for Film and Music       | K    | <<Output Truncated>>                                       |
| 24Q560 | Robert F. Wagner, Jr. Secondary School for Art... | Q    | <<Output Truncated>>                                       |
| 11X290 | Bronx Academy of Health Careers                   | X    | <<Output Truncated>>                                       |
| 09X250 | Eximius College Preparatory Academy: A College... | X    | <<Output Truncated>>                                       |
| 03M417 | Frank McCourt High School                         | M    | <<Output Truncated>>                                       |

### A Problem that was presented in the data

A major problem presented was the presence of empty columns as well as categorical columns. I removed the categorical columns by selecting the number dtypes to be included. I removed empty columns by filtering out columns that contained too many NA values.

### Links:

[Original Raw Data](data/2019_DOE_High_School_Directory_20240219.csv)

[Munged Data](data/cleaned_data.csv)

[Spreadsheet Data](data/cleaned_data.xlsx)

## Analysis

### Agregated Statistics:

Average of Graduation Rate: 0.79

Maximum of Attendance Rate: 0.98

Minimum of College Career Rate: 0.15

Count of schools with Student Safety Rate < 0.8: 293

## Markdown Table for Pivot Table

| School Name                                                      | College Career Rate | Pct Stu Enough Variety | Attendance Rate | Graduation Rate | Pct Stu Safe |
| ---------------------------------------------------------------- | ------------------- | ---------------------- | --------------- | --------------- | ------------ |
| Archimedes Academy for Math, Science and Technology Applications | 0.43                | 0.59                   | 0.78            | 0.63            | 0.70         |
| Bronx Career and College Preparatory High School                 | 0.29                | 0.76                   | 0.76            | 0.43            | 0.82         |
| Bronx Design and Construction Academy                            | 0.38                | 0.67                   | 0.76            | 0.54            | 0.51         |
| Brooklyn Frontiers High School                                   | 0.59                | 0.68                   | 0.76            | 0.79            | 0.79         |
| Brooklyn Lab School                                              | 0.42                | 0.77                   | 0.79            | 0.63            | 0.77         |
| Brooklyn School for Social Justice, The                          | 0.48                | 0.64                   | 0.78            | 0.69            | 0.74         |
| Dr. Susan S. McKinney Secondary School of the Arts               | 0.45                | 0.79                   | 0.76            | 0.69            | 0.85         |
| East Bronx Academy for the Future                                | 0.57                | 0.67                   | 0.79            | 0.78            | 0.82         |
| East Williamsburg Scholars Academy                               | 0.30                | 0.75                   | 0.77            | 0.64            | 0.82         |
| Frederick Douglass Academy III Secondary School                  | 0.34                | 0.65                   | 0.76            | 0.73            | 0.83         |
| Gotham Professional Arts Academy                                 | 0.50                | 0.64                   | 0.78            | 0.55            | 0.76         |
| High School for Violin and Dance                                 | 0.43                | 0.56                   | 0.71            | 0.67            | 0.75         |
| Hudson High School of Learning Technologies                      | 0.54                | 0.76                   | 0.79            | 0.64            | 0.83         |
| Jacqueline Kennedy Onassis High School                           | 0.46                | 0.41                   | 0.79            | 0.64            | 0.80         |
| Marta Valle High School                                          | 0.49                | 0.64                   | 0.79            | 0.74            | 0.89         |
| Metropolitan High School, The                                    | 0.43                | 0.60                   | 0.76            | 0.50            | 0.68         |
| Metropolitan Soundview High School, The                          | 0.53                | 0.69                   | 0.79            | 0.63            | 0.77         |
| Mott Haven Village Preparatory High School                       | 0.48                | 0.65                   | 0.78            | 0.53            | 0.83         |
| Murray Hill Academy                                              | 0.59                | 0.76                   | 0.79            | 0.79            | 0.90         |
| Nelson Mandela High School                                       | 0.59                | 0.60                   | 0.78            | 0.79            | 0.81         |
| School for Excellence                                            | 0.35                | 0.59                   | 0.66            | 0.58            | 0.79         |
| School for Tourism and Hospitality                               | 0.42                | 0.56                   | 0.77            | 0.55            | 0.81         |
| The Brooklyn Academy of Global Finance                           | 0.26                | 0.76                   | 0.78            | 0.66            | 0.85         |
| Validus Preparatory Academy                                      | 0.45                | 0.69                   | 0.79            |

## Short Description

THis Povit Table filters the schools with all rating less than 80%, which gives an insight of the majority of these "bad schools" are located in Brooklyn and Bronx that are most likely to be impoverished.
