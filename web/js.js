eel.call_js()
async function addt_fds() {
    var time=  eel.startTime()
    var res=await time()
    
    var bo=`<p> ${res}</p>`
    document.body.insertAdjacentHTML("beforebegin",bo)
    
   }


eel.expose(add_time);
function add_time(go,come,remain){
    var go_date=`<h1>${go}</h1>`
    var come_date= `<h1>${come}</h1>`
    var remain_time=`<h1>${remain}</h1>`
    // $("#content").append(go_date)
    $("#go").html(go_date);
    $("#arrive").html(come_date);
    $("#remain").html(remain_time);
    console.log($("#content"));
}
