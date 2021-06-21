import React from 'react';
import TodoItem from './todo';


const TodoListView = (props) => {
    return ( 
    <div>
        <ul>
            {props.todoList.map(todo => <TodoItem key={todo._id} todo={todo} />)}
        </ul>
    </div> );
}
 
export default TodoListView;