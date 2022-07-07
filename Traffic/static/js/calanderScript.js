const date = new Date();

document.querySelector('.event-heading p').innerHTML = new Date().toDateString();


const loadCalander =()=>{
    const monthDays= document.querySelector(".days")
    date.setDate(1);
    
    const lastDay = new Date(date.getFullYear(),date.getMonth()+1,0).getDate();
    
    const prevLastDay=new Date(date.getFullYear(),date.getMonth(),0).getDate();
    const lastDayIndex =new Date(date.getFullYear(),date.getMonth()+1,0).getDay();
    const nextDay= 7-lastDayIndex-1;
    
    const firstDayIndex = date.getDay();
    const months= [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ];

    document.querySelector(".date h1").innerHTML =months[date.getMonth()];
    
    document.querySelector('.date p').innerHTML = new Date().toDateString();
    
    let days="";
    
    for(let i=firstDayIndex; i>0;i--){
        days +=`<div class='prev-date'>${prevLastDay-i+1}</div>`;
    }
    
    for (let i=1; i<=lastDay;i++){
        if(i=== new Date().getDate() && date.getMonth()===new Date().getMonth()){
            days += `<div class='today'>${i}</div>`
    
        }else{
            days += `<div class="days-date">${i}</div>`
    
        } 
    
    }
    
    for(let j=1;j<=nextDay;j++){
        days+=`<div class="next-date">${j}</div>`
    
    }
    monthDays.innerHTML=days;


    // Selected Date
    document.querySelectorAll('.days-date').forEach(iteam => {
        iteam.addEventListener('click',()=>{
            var selectedMonth = document.querySelector('.date h1').innerHTML;
            var selectedDate = iteam.textContent;
            var selectedYear = date.getFullYear();
            var selected = `${selectedYear} \ ${selectedMonth} \ ${selectedDate}`;
    
            let d = new Date(`${selectedMonth} ${selectedDate} `);
    
            document.querySelector(".event-heading p").innerHTML=selected;
        
        });
    
    });
    

}



document.querySelector('.prev').addEventListener('click',()=> {
    date.setMonth(date.getMonth()-1);
    loadCalander();

});

document.querySelector('.next').addEventListener('click',()=> {
    date.setMonth(date.getMonth()+1);
    loadCalander();


});

loadCalander();

document.querySelector('.mobile-event').addEventListener('click',()=>{
    var calender = document.getElementById('calender').classList.add('displayNoneCalender');
    var mobileremonder = document.getElementById('mobile-event').classList.add('displayNoneMobileReminder');
    var mobilecalander =document.getElementById('mobile-calander').classList.add('displayNavCalander');
    var reminder = document.getElementById('event').classList.add('displayNavEvent')
});

document.querySelector('.mobile-calander').addEventListener('click',()=>{
    var calender = document.getElementById('calender').classList.remove('displayNoneCalender');
    var mobileremonder = document.getElementById('mobile-event').classList.remove('displayNoneMobileReminder');
    var mobilecalander =document.getElementById('mobile-calander').classList.remove('displayNavCalander');
    var reminder = document.getElementById('event').classList.remove('displayNavEvent')
});

