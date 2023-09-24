# Premier League Team Quiz

#### Video Demo:  <https://youtu.be/OS4DlCuPtRw>

#### Access Link: <https://premierleagueteamquiz.pythonanywhere.com/>

#### Description:

This quiz allows users to find which Premier League Teams they should support based on their personality. 

It is implemented through a database of 16 teams, and every time the user starts the quiz, their scores get reset to zero.
They will be asked a series of questions, every answer will increment scores for the team that fits the answer the most.

When the user submits his/her answers, a SQL query will look for the team with the highest compatibility score and output it to the screen.

#### User Greeting:

>Are you unsure about which team to support? 
>
>It is commonplace to support your local team or whatever team your family has ties to, but what if you're on the other side of the world and no one in your family likes football?
>
>Take this short quiz to find out which team you should really support based on your personality, even if you already support a team!
>
>Assuming you'd want to watch games on TV or online, we won't be recommending teams from lower divisions or teams flirting with relegation every year, going down and coming back up the next (also known as a yo-yo club, such as Norwhich City). 
>
>Furthermore, we won't be taking Burnley into account, as they play some of the most boring and depressive football you'll ever see and their own fans will be the first ones to admit it. They do make up for it by being some of the most dedicated fans out there though, but it's just not a team you'd want to be supporting if you're overseas as there are many more exciting options.
>
>Keep in mind that if you're unsure, you don't have to answer every single question for the test to work.

#### Teams In The Database:

- Arsenal
- Aston Villa 
- Brentford
- Brighton 
- Chelsea 
- Everton
- Leeds
- Leicester 
- Liverpool 
- Manchester City 
- Manchester United 
- Newcastle United 
- Southampton 
- Tottenham Hotspur 
- West Ham United 
- Wolverhampton Wanderers


#### Implementation:

The way I've implemented this is that I have a database with a list of all Premier League teams, except some teams that get relegated often and I've given them a score, whose default value is zero.

Every team has a unique id representing it and I have also paired every answer to each question with a list of ids.

As you start taking the quiz, you'll be asked a wide range of questions, whose main target is to gauge what kind of person you are and to find some personality traits.


Once you've gone through all the questions, whether you've answered them or not, by clicking on the submit button, the app will look at your answers, which each contain a list of integers, representing the ids of teams that fit the answer you selected, and append the seperate lists into a big list.

Next, the app will loop through that list and for each integer, add a certain number of points to the compatibility score of each team in the database.

It will then return which team has the highest compbatibility score, and output the name of said team below its emblem.
