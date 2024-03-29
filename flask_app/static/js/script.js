const currentDateEl = document.querySelector('.current-date');
const statusCardsEl = document.querySelectorAll('.status-card');
const listTablesEl = document.querySelectorAll('.list-table');
const manageTeamsInputsEl = document.querySelectorAll('.manage-teams-input');
const deleteActionButtonsEl = document.querySelectorAll('.delete-action-button');
const createTeamButtonEl = document.querySelector('#create-team-form-submit-button');
const editTeamNameButtonsEl = document.querySelectorAll('.edit-team-name-button');

// Render today's date in 'M/DD/YYYY' format
const renderToday = () => {
    const today = new Date().toLocaleDateString('en-US', { timeZone: 'UTC' }).slice(0, 10);

    return currentDateEl.innerText = today + " (UTC)";
};

// Render numbers of task for task status cards on dashboard page
const renderStatusData = () => {
    const userListTableEl = document.querySelector('#user-list-table');
    const totalNumOfUserTasksEl = document.querySelector('#total-num-of-user-tasks');
    const numOfUserTasksToDoEl = document.querySelector('#num-of-user-tasks-to-do');
    const numOfUserTasksInProgressEl = document.querySelector('#num-of-user-tasks-in-progress');
    const numOfUserTasksDoneEl = document.querySelector('#num-of-user-tasks-done');
    const numOfUserOverdueTasksEl = document.querySelector('#num-of-user-overdue-tasks');

    const teamListTableEl = document.querySelector('#team-list-table');
    const totalNumOfTeamTasksEl = document.querySelector('#total-num-of-team-tasks');
    const numOfTeamTasksToDoEl = document.querySelector('#num-of-team-tasks-to-do');
    const numOfTeamTasksInProgressEl = document.querySelector('#num-of-team-tasks-in-progress');
    const numOfTeamTasksDoneEl = document.querySelector('#num-of-team-tasks-done');
    const numOfTeamOverdueTasksEl = document.querySelector('#num-of-team-overdue-tasks');

    if (userListTableEl) {
        totalNumOfUserTasksEl.innerText = userListTableEl.querySelectorAll('tbody > tr').length;
        numOfUserTasksToDoEl.innerText = userListTableEl.querySelectorAll(`[class*="to-do-icon"]`).length;
        numOfUserTasksInProgressEl.innerText = userListTableEl.querySelectorAll(`[class*="in-progress-icon"]`).length;
        numOfUserTasksDoneEl.innerText = userListTableEl.querySelectorAll(`[class*="done-icon"]`).length;
        numOfUserOverdueTasksEl.innerText = userListTableEl.querySelectorAll(`[data-overdue*="true"]`).length;
    };

    if (teamListTableEl) {
        totalNumOfTeamTasksEl.innerText = teamListTableEl.querySelectorAll('tbody > tr').length;
        numOfTeamTasksToDoEl.innerText = teamListTableEl.querySelectorAll(`[class*="to-do-icon"]`).length;
        numOfTeamTasksInProgressEl.innerText = teamListTableEl.querySelectorAll(`[class*="in-progress-icon"]`).length;
        numOfTeamTasksDoneEl.innerText = teamListTableEl.querySelectorAll(`[class*="done-icon"]`).length;
        numOfTeamOverdueTasksEl.innerText = teamListTableEl.querySelectorAll(`[data-overdue*="true"]`).length;
    };
};

// Render to-do list table row ids on dashboard page
const renderTableRowId = () => {
    listTablesEl.forEach((table) => {
        table.children[1].querySelectorAll('.table-body-row').forEach((row, i) => {
            row.querySelector('.table-row-id').innerText = i + 1;
        });
    });
};

// Render to-do list table's task status icons on dashboard page
const renderStatusIcon = () => {
    const statusTds = document.querySelectorAll(`[class*="status-td"]`);

    statusTds.forEach(td => {
        switch (td.innerText) {
            case "To do":
                td.querySelector('.status-icon').className = "to-do-icon";
                break;
            case "In progress":
                td.querySelector('.status-icon').className = "in-progress-icon";
                break;
            case "Done":
                td.querySelector('.status-icon').className = "done-icon";
                break;
        }
    })
};

// Render task due date in 'M/DD/YYYY' format on dashboard page
const formatDueDate = () => {
    const dueDateTds = document.querySelectorAll(`[class*="due-date-td"]`);

    dueDateTds.forEach(td => {
        const newFormatDate = new Date(td.innerText).toLocaleDateString('en-US', { timeZone: 'UTC' }).slice(0, 10);
        td.innerText = newFormatDate;
    })
};

// Render the overdue date in red on dashboard page
const checkOverdue = () => {
    const today = new Date()
    const dueDateTds = document.querySelectorAll(`[class*="due-date-td"]`);

    dueDateTds.forEach(td => {
        const dueDate = new Date(td.innerText)
        if (td.previousElementSibling.innerText !== "Done" && today.getTime() > dueDate.getTime()) {
            td.style.color = "var(--highlight1)";
            td.setAttribute("data-overdue", "true");
        }
    })
};

// Show confirm message before deleting a task on dashboard page
const confirmDelete = () => {
    return confirm("Are you sure you want to delete this task?");
};

// Remove success message on manage teams page
const removeSuccessMessage = (e) => {
    if (e.target.parentNode.querySelector(`[class*="success-message"]`)) {
        const message = e.target.parentNode.querySelector(`[class*="success-message"]`);
        message.remove();
    }
};

// Render input field to change the team name when edit button is clicked
const renderEditTeamNameInputField = (e) => {
    const editButton = e.target;
    editButton.style.visibility = "hidden";

    const teamNameTd = editButton.parentElement.parentElement.previousElementSibling.querySelector('.team-name-td');
    const formContainer = editButton.parentElement.parentElement.previousElementSibling.querySelector('.edit-team-name-form-container');
    const cancelButton = editButton.parentElement.parentElement.previousElementSibling.querySelector('.cancel-edit-team-name-button');

    teamNameTd.style.display = "none";
    formContainer.style.display = "block";

    cancelButton.addEventListener('click', function () {
        editButton.style.visibility = "visible";
        teamNameTd.style.display = "block";
        formContainer.style.display = "none";
    })

}

if (currentDateEl) {
    document.addEventListener('DOMContentLoaded', renderToday);
};

if (listTablesEl) {
    document.addEventListener('DOMContentLoaded', function () {
        renderTableRowId();
        renderStatusIcon();
        formatDueDate();
        checkOverdue();
    });
};

if (statusCardsEl) {
    document.addEventListener('DOMContentLoaded', renderStatusData);
};

if (deleteActionButtonsEl) {
    deleteActionButtonsEl.forEach((button) => {
        button.addEventListener('click', confirmDelete);
    });
};

if (manageTeamsInputsEl) {
    manageTeamsInputsEl.forEach((input) => {
        input.addEventListener('click', removeSuccessMessage);
    });
};

if (editTeamNameButtonsEl) {
    editTeamNameButtonsEl.forEach((button) => {
        button.addEventListener('click', renderEditTeamNameInputField);
    });
};