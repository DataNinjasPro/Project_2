var todos = [
  {
    complete: false,
    text: "Learn JavaScript"
  },
  {
    complete: false,
    text: "Learn JavaScript Charting"
  },
  {
    complete: false,
    text: "Make Awesome Front-End Projects"
  }
];

// Getting references to button and input field
var addTodoBtn = document.querySelector("#add-todo");

// renderTodos puts the todo list items on the page
function renderTodos() {
  var todoList = document.querySelector("#todo-list");

  for (var i = 0; i < todos.length; i++) {
    var todo = todos[i];
    var todoItem = document.createElement("li");

    todoItem.innerHTML = todo.text;
    todoList.appendChild(todoItem);
  }
}

// Rendering the list of todos to the DOM
renderTodos();

addTodoBtn.addEventListener("click", function(event) {
  // Retrieve todoInput and todoList elements
  var todoInput = document.querySelector("#todo-input");
  var todoList = document.querySelector("#todo-list");

  // When the todo button is clicked, capture the value of the text in the input
  var inputText = todoInput.value;

  // Use the Array push method to add the new todo to the array of todos
  var todo = {
    text: inputText,
    complete: false
  };

  todos.push(todo);

  if (todos.length > 5) {
    alert("Are you sure will have enough time to get all these done?!");
  }

  // Add todoItem to list
  var todoItem = document.createElement("li");

  todoItem.innerHTML = todo.text;
  todoList.appendChild(todoItem);

  // Clear the value of the input field
  todoInput.value = "";
});
