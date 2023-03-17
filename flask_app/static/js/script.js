const renderToday = () => {
    const today = new Date().toLocaleDateString('en-US', {timeZone: 'UTC'}).slice(0, 10);
    return document.getElementById("current-date").innerHTML = today;
};

const renderSummaryNums = () => {
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


    totalNumOfUserTasksEl.innerText = userListTableEl.querySelectorAll('tbody > tr').length;
    numOfUserTasksToDoEl.innerText = userListTableEl.querySelectorAll(`[class*="to-do-icon"]`).length;
    numOfUserTasksInProgressEl.innerText = userListTableEl.querySelectorAll(`[class*="in-progress-icon"]`).length;
    numOfUserTasksDoneEl.innerText = userListTableEl.querySelectorAll(`[class*="done-icon"]`).length;
    numOfUserOverdueTasksEl.innerText = userListTableEl.querySelectorAll(`[data-overdue*="true"]`).length;

    totalNumOfTeamTasksEl.innerText = teamListTableEl.querySelectorAll('tbody > tr').length;
    numOfTeamTasksToDoEl.innerText = teamListTableEl.querySelectorAll(`[class*="to-do-icon"]`).length;
    numOfTeamTasksInProgressEl.innerText = teamListTableEl.querySelectorAll(`[class*="in-progress-icon"]`).length;
    numOfTeamTasksDoneEl.innerText = teamListTableEl.querySelectorAll(`[class*="done-icon"]`).length;
    numOfTeamOverdueTasksEl.innerText = teamListTableEl.querySelectorAll(`[data-overdue*="true"]`).length;


};

const renderTableRowId = () => {
    const userListTableEl = document.querySelector('#user-list-table');
    const userListTableRows = userListTableEl.querySelectorAll('tbody > tr');
    userListTableRows.forEach((row, i) => {
        row.querySelector('.table-row-id').innerText = i + 1;
    })

    const teamListTableEl = document.querySelector('#team-list-table');
    const teamListTableRows = teamListTableEl.querySelectorAll('tbody > tr');
    teamListTableRows.forEach((row, i) => {
        row.querySelector('.table-row-id').innerText = i + 1;
    })
};

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

const formatDueDate = () => {
    const dueDateTds = document.querySelectorAll(`[class*="due-date-td"]`);
    dueDateTds.forEach(td => {
        const newFormatDate = new Date(td.innerText).toLocaleDateString('en-US', {timeZone: 'UTC'}).slice(0, 10);
        td.innerText = newFormatDate;
    })
};

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

const confirmDelete = () => {
    return confirm("Are you sure you want to delete?");
};

const handleAssignee = () => {
    const taskCategoryVal = document.querySelector('.task-category').value;
    const assignDefaultOption = document.querySelector('.assign-default-option');
    const assignMyselfOption = document.querySelector('.assign-myself-option');
    const assignOthersOptions = document.querySelectorAll('.assign-others-option');

    switch (taskCategoryVal) {
        case "Private":
            console.log("test");
            assignDefaultOption.removeAttribute("selected");
            assignMyselfOption.setAttribute("selected", "selected");
            assignOthersOptions.forEach(option => {
                option.setAttribute("disabled", "disabled")
            });
            break;
        case "Public":
            assignOthersOptions.forEach(option => {
                option.removeAttribute("disabled")
            });
            assignMyselfOption.removeAttribute("selected");
            assignDefaultOption.setAttribute("selected", "selected");
    }
};

const disableAssigneeOptions = () => {
    const editTaskCategoryVal = document.querySelector('#edit-task-category').value;
    const assignOthersOptions = document.querySelectorAll('.assign-others-option');

    if (editTaskCategoryVal === 'Private') {
        assignOthersOptions.forEach(option => {
            option.setAttribute("disabled", "disabled")
        });
    };
};

if (document.getElementById("current-date")) {
    renderToday();
};

if (document.querySelector('#user-list-table') && document.querySelector('#team-list-table')) {
    renderTableRowId();
    renderStatusIcon();
    formatDueDate();
    checkOverdue();
    renderSummaryNums();
};

if (document.querySelector('#edit-task-category')) {
    disableAssigneeOptions();
};