## April 1 2026

- n rotations all in a single direction are enough to cover all possible rotaitons
- We need to indentify the maximum matchings over all those rotations
- Since each mathcing corresponds to exactly rotation I calculated which rotaion each corresponds to.
- Then in those I chose the most frequent one, hence that would lead to the maximum matching. 

- One way would be to count the matches for each rotation but that has a high time complexity because, For each element in b there is only one roatiton which can leads it be mathced but we keep on verfying if it has been mathced or not for every rotation. I feel like we will need to anyway calculate how many rotations each element needs to find its partner.( It might be that this approach works but my algorithm for that is inefficient, If anyone was able to do so please lemme know on discord)
