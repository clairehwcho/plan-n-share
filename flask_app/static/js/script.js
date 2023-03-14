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

const confirm_delete = () => {
    return confirm("Are you sure you want to delete?");
};

if (document.getElementById("current-date")) {
    render_today();
};