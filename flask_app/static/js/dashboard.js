const render_today = () => {
    const today = new Date();
    const dayList = ["Sunday", "Monday", "Tuesday", "Wednesday ", "Thursday", "Friday", "Saturday"];
    const monthList = ["January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"];

    const day = dayList[today.getDay()];
    const month = monthList[today.getMonth()];
    const date = today.getDate();
    const year = today.getFullYear();
    return document.getElementById("current-date").innerHTML = "&nbsp;" + day + ", " + month + " " + date + ", " + year;
};

const render_summary_nums = () => {
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

const render_table_row_id = () => {
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

const render_status_icon = () => {
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

const check_overdue = () => {
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

const confirm_delete = () => {
    return confirm("Are you sure you want to delete?");
};

render_today();
render_table_row_id();
render_status_icon();
check_overdue();
render_summary_nums();