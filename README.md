# Gilded rose tech test

This is a well known kata developed by Terry Hughes. This is commonly used as a tech test to assess a candidate's ability to read, refactor and extend legacy code.

Here is the text of the kata:

*"Hi and welcome to team Gilded Rose. As you know, we are a small inn with a prime location in a prominent city run by a friendly innkeeper named Allison. We also buy and sell only the finest goods. Unfortunately, our goods are constantly degrading in quality as they approach their sell by date. We have a system in place that updates our inventory for us. It was developed by a no-nonsense type named Leeroy, who has moved on to new adventures. Your task is to add the new feature to our system so that we can begin selling a new category of items. First an introduction to our system:

All items have a SellIn value which denotes the number of days we have to sell the item. All items have a Quality value which denotes how valuable the item is. At the end of each day our system lowers both values for every item. Pretty simple, right? Well this is where it gets interesting:

Once the sell by date has passed, Quality degrades twice as fast
The Quality of an item is never negative
“Aged Brie” actually increases in Quality the older it gets
The Quality of an item is never more than 50
“Sulfuras”, being a legendary item, never has to be sold or decreases in Quality
“Backstage passes”, like aged brie, increases in Quality as it’s SellIn value approaches; Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but Quality drops to 0 after the concert
We have recently signed a supplier of conjured items. This requires an update to our system:

“Conjured” items degrade in Quality twice as fast as normal items
Feel free to make any changes to the UpdateQuality method and add any new code as long as everything still works correctly. However, do not alter the Item class or Items property as those belong to the goblin in the corner who will insta-rage and one-shot you as he doesn’t believe in shared code ownership (you can make the UpdateQuality method and Items property static if you like, we’ll cover for you)."*

## Project approach
To solve this test I used Python and Unittest.

To solve this tech test I used the main principles of OOP: inheritance and polymorphism.<br> 
The main goal in the test was the ability to add new items to the system without needing to change the code that updates sell in and quality every time.<br>
As all items have the same attributes (sell-in and quality) and method (update quality) this gave me an understanding that the inheritance principle must be used.<br>
However, several items (aged brie, sulfuras, and backstage passes) have slightly different rules in the way the update quality method would work for them. 
Hence, here we can use another OOP principle - polymorphism.<br>

In my solution, I introduced children classes that inherit from the parent item class. This was needed so I could reuse all the same attributes 
from the parent class, but change the update quality method.<br>

If new items need to be added to the store and the way their quality updates are different from the main item, this can be done by adding
a new class and changing the update quality method.<br>

When the quality update is needed, all items can be created from the corresponding classes and passed as an argument to the gilded rose class.
Then the update quality method can be called. As the update quality method is slightly different for different children's classes, the 
quality will be updated according to the rules.

💙 I really enjoyed the test, it was fun to learn about inheritance and polymorphism through a good example! 

## Table of Contents

The test consists of the following files:
1. gilded_rose.py - the original code of the test.
2. gilded_rose_soltution.py - my solution to the gilded rose test.
3. item.py, aged_brie.py, sulfuras.py and backstage.py - one file for each of the corresponding items: parent class: item, children: aged brie, sulfuras and backstage.
4. Test files: 1 integration test and 4 files for unit test for each of the classes.

## Project Dependencies
1. Install the latest Python version
2. Install Unittest

## How to use the project
First, create item objects from the desired classes with the initial sell_in and quality values. Add the items to a list and assign the list to a variable, e.g.<br>
`items = [AgedBrie(0, 0),Sulfuras(3, 1),BackstagePasses(3, 1),Item(5,2)]`

Create a Gilded rose object from the class and pass the array with the items created on the previous stage:<br>
`gilded_rose = GildedRose(items)`

To update the quality and the sell in, run the following method:<br>
`gilded_rose.update_quality()`

To run the tests use the following command: <br>
`python` + the name of the test file you would like to run, e.g. `python test_integration.py`

