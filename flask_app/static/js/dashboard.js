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
    const userListTable = document.querySelector('#user-list-table');
    const totalNumOfUserTasks = document.querySelector('#total-num-of-user-tasks');
    const numOfUserTasksToDo = document.querySelector('#num-of-user-tasks-to-do');
    const numOfUserTasksInProgress = document.querySelector('#num-of-user-tasks-in-progress');
    const numOfUserTasksDone = document.querySelector('#num-of-user-tasks-done');

    const teamListTable = document.querySelector('#team-list-table');
    const totalNumOfTeamTasks = document.querySelector('#total-num-of-team-tasks');
    const numOfTeamTasksToDo = document.querySelector('#num-of-team-tasks-to-do');
    const numOfTeamTasksInProgress = document.querySelector('#num-of-team-tasks-in-progress');
    const numOfTeamTasksDone = document.querySelector('#num-of-team-tasks-done');

    let countUserTaskToDo = 0;
    let countUserTaskInProgress = 0;
    let countUserTaskDone = 0;

    let countTeamTaskToDo = 0;
    let countTeamTaskInProgress = 0;
    let countTeamTaskDone = 0;

    userListTable.querySelectorAll('tbody > tr > td')
        .forEach(td => {
            switch (td.innerText) {
                case "To do":
                    countUserTaskToDo++;
                    break;
                case "In progress":
                    countUserTaskInProgress++;
                    break;
                case "Done":
                    countUserTaskDone++;
                    break;
            }
        })

    teamListTable.querySelectorAll('tbody > tr > td')
        .forEach(td => {
            switch (td.innerText) {
                case "To do":
                    countTeamTaskToDo++;
                    break;
                case "In progress":
                    countTeamTaskInProgress++;
                    break;
                case "Done":
                    countTeamTaskDone++;
                    break;
            }
        })


    totalNumOfUserTasks.innerText = userListTable.querySelectorAll('tbody > tr').length;
    numOfUserTasksToDo.innerText = countUserTaskToDo;
    numOfUserTasksInProgress.innerText = countUserTaskInProgress;
    numOfUserTasksDone.innerText = countUserTaskDone;

    totalNumOfTeamTasks.innerText = teamListTable.querySelectorAll('tbody > tr').length;
    numOfTeamTasksToDo.innerText = countTeamTaskToDo;
    numOfTeamTasksInProgress.innerText = countTeamTaskInProgress;
    numOfTeamTasksDone.innerText = countTeamTaskDone;
}

const confirm_delete = () => {
    return confirm("Are you sure you want to delete?");
};

render_today();
render_summary_nums();