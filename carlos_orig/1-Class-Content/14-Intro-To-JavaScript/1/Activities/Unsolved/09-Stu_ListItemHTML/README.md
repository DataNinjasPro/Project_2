# List Item HTML

In this activity we will render an unordered list in the DOM to hold each element in the `todos` array.

## Instructions

Open [index.js](Unsolved/index.js) and add code to the `renderTodos` function to accomplish the following:

1. In `index.html`, there is a DOM element with an `id` of `todo-list`. In `index.js`, store a reference to the DOM element into a variable named `$todoList`. Accomplish this using the `document.querySelector` method. 

2. Create a variable and set it to an empty string named `todoHTML`.

3. Using a for-loop, iterate through each object in the `todos` array.

4. For each object in the `todos` array, write code to append an `li` tag containing the `text` property of each object to the `todoHTML` string variable. You will need to use the concatenation operator to accomplish this.

5. After iterating though each object in the `todos` array, write code to set the `innerHTML` of the `$todoList` element to the `todoHTML` string we've been building. 

## Hints

* Check out [MDN's Docs on Element.innerHTML](https://developer.mozilla.org/en-US/docs/Web/API/Element/innerHTML)

* Check out [MDN's Docs on document.querySelector](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector)
