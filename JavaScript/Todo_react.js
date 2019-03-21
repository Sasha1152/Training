import React from 'react';
import './Todo.css'

class Todo extends React.Component {
  state = {
    todos: [
        { id: 1, text: 'learn react', done: true },
        { id: 2, text: 'build an react app', done: false },
        { id: 3, text: 'modify', done: true },
        { id: 4, text: 'test', done: false },
    ],
    text: '',
    filter: ''
  }
  
handleChange = (id) => { 
  let todos_new = this.state.todos.map((todo) => {
    if (todo.id === id){
      todo.done = !todo.done;
    }
    return todo;
  });
  return this.setState({
    todos: todos_new
  });
}

removeMethod = (id) => {
  this.setState({
    todos: this.state.todos.filter(obj => !String(obj.id).includes(String(id)))
  })
}

showList = () => {
    return (
      <div>
        {this.state.todos.map((todo) => (<li className={`done-${todo.done}`}><input type="checkbox" onChange={() => this.handleChange(todo.id)} checked={todo.done}/>{todo.text} <span onClick={() => this.removeMethod(todo.id)}><a href="#">remove</a></span></li>) )}
      </div>
    );
}

addElem = (event) => {
  event.preventDefault()
  this.setState({
    todos: [...this.state.todos, {id: Date.now(), text: document.getElementById('input1').value, done: false}]
  })
  document.getElementById('input1').value = ''
}

findMethod = () => {
  this.setState({
    todos: this.state.todos.filter(obj => obj.text.includes(document.getElementById('input2').value))
    })
}

deleteMethod = () => {
  this.setState({
    todos: this.state.todos.filter(obj => !obj.done)
  })
}
  render() {
    return (
      <div className="Todo">
        <h2>Todo</h2>
        <div>
          <input type="text" id="input2" placeholder="filter tasks" onChange={this.findMethod}/>
          <br />
          <span>{this.state.todos.length} remaining </span>
        </div>
        <ul>
          {this.showList()}
        </ul>

        <form>
          <input type="text" id="input1"/>
          <button type="submit" onClick={this.addElem}>Add</button>
        </form>

        <a href="#" onClick={this.deleteMethod}>clean</a>
      </div>
    );
  }
}

export default Todo;
