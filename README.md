# Ex1
Our project presents an implementation of the offline algorithm of a smart elevator system in a high-rise building, using an efficient data structure with the aim that the entire waiting for the elevator will be reduced to a minimum.

-**First link:** https://e-space.mmu.ac.uk/617034/1/WCE2016_pp671-673.pdf The article shows the problems that currently exists with the unwise elevators, such as congestion inside one of the elevators or Long time of waiting and standing inside the elevator. The article shows a solution that uses Artificial intelligence, and although in this task we do not touch artificial intelligence, the article helps us understand the The main problems that there are in the elevators are old and thus helps us find an effective solution that will solve these problems.

-**second link:** https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9003300 This article conducts an experiment in which simulations are used to verify the effectiveness of their solution to a smart elevator. The simulator records the waiting time, travel time and number of passengers in the elevator. The experiment uses a comparison between their access to smart elevators and approaches of older elevators to see if there really is efficiency in a smart elevator. The results of the experiment do show that smart elevators are more efficient in terms of waiting time than older elevators. This article helped us understand how to test our algorithm and how to make sure it's effective in relation to unwise elevators.

-**three link:** https://www.cs.huji.ac.il/~ai/projects/2014/The_intelevator/files/report.pdf This article talks about online algorithms versus offline algorithms for the problem of elevator scheduling , The article presents the problem of scheduling the elevator "in the best possible way" which online algorithm is best suited , and to define the best interests of the offline algorithm, this article helps us understand the deliberate and unintentional algorithm that we are required to write in part of the task.

## The off-line algorithm: 
the main idea of the algorithm is to generate from all the calls we received as many routes as possible and divide them equally between the elevators.
Route definition: calls A and B on the same route is they both travel in the same direction , both have the same destination, the elevator does not have to change the direction to reach on of them, its mean that if the direction of the calls is up and the call A was called first them I need to check if the source floor of B more height from the source floor of A, when the direction is down I need to check  if the source floor of B more lower from the source floor of A.
In addition, in order for both calls to be on the same route assuming that A call was made first, we need to make sure that the time of call A + the time it takes to get from the source floor of A to the source floor of B is greater or equal then the time of call B, in this way we will make sure that the elevator has not yet passed the source floor of B.
implementation: each call receives a specific id, the calls that are on the same route with the same id. In this way, when we want to put a call in rout, we can put it in the exact location so that we go through all the calls with the same id and put the call in the right location.
Each elevator has a 'list' field where there is a list of all the calls it needs to make.
After we divide into the routs we will put each route or a single call into the elevator in such a way that we divide the callss evenly, meaning that we will go through all the elevators and put the call or route into the elevator with the least readings.

## UML
![WhatsApp Image 2021-11-18 at 13 23 38](https://user-images.githubusercontent.com/93201414/142408929-597ab686-f42f-43cf-b155-5fd1b5566ede.jpeg)

