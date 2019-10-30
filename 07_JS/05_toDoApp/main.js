// card 만들기
function init() {
    const button = document.querySelector('#js-todo-button');
    const inputArea = document.querySelector('#js-todo-input');
    const reverseBtn = document.querySelector('#js-reverse-btn');

    reverseBtn.addEventListener('click', () => {
        const todoArea = document.querySelector('#js-todo-area');
        const todos = Array.from(document.querySelectorAll('.js-card'));

        while (todoArea.firstChild) {
            todoArea.removeChild(todoArea.firstChild);
        }

        todos.reverse().forEach((todo) => {
            todoArea.appendChild(todo)
        });

    })

    button.addEventListener('click', () => {
        const inputArea = document.querySelector('#js-todo-input');
        createTodoCard(inputArea.value);
        inputArea.value = null;
    })

    inputArea.addEventListener('keydown', (e) => {
        if (e.which === 13) {
            const inputArea = document.querySelector('#js-todo-input');
            createTodoCard(inputArea.value);
            inputArea.value = null;
        }
    })

    const createTodoCard = (content, completed = false) => {
        const cardArea = document.querySelector('#js-todo-area');

        const todo = document.createElement('div');
        todo.className = 'ui segment js-card';

        const wrapper = document.createElement('div');
        wrapper.className = 'ui checkbox';

        const checkBox = document.createElement('input');
        checkBox.type = 'checkbox';

        checkBox.addEventListener('click', () => {
            const checked = checkBox.checked
            if (checked) {
                todo.classList.add('secondary');
                label.classList.add('done');
            } else {
                todo.classList.remove('secondary');
                label.classList.remove('done');
            }
        })

        const label = document.createElement('label');
        label.innerHTML = content;

        const deleteIcon = document.createElement('i');
        deleteIcon.className = 'icon close custom-icon';

        deleteIcon.addEventListener('click', () => {
            cardArea.removeChild(todo);
        })

        wrapper.appendChild(checkBox);
        wrapper.appendChild(label);
        todo.appendChild(wrapper);
        todo.appendChild(deleteIcon);
        cardArea.appendChild(todo);
    }
}

init();