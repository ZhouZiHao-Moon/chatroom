function enter()
{
    var name = $("#name").val();
    $("#name").attr("disabled","disabled");
    $("#enter").attr("disabled","disabled");
    $("#text").removeAttr("disabled");
    $("#send").removeAttr("disabled");
    $("#text").val("[系统提示]已经进入聊天室");
    send();
    setInterval('refresh(false)',1000);
}
function refresh(roll)
{
    var time = $("#time").text();
    $.post("refresh/",{"time":time},function(data){
        data = eval('('+data+')');
        $('#time').text(data[0]['time']);
        for(var i=1;i<data.length;i++)
        {
            var name = data[i]['name'];
            var text = data[i]['text'];
            var t = parseInt(data[i]['time']);
            var time = new Date(t).toLocaleString();
            $("#message").append("<p><b>"+name+"</b>&nbsp;&nbsp;&nbsp;&nbsp;"+time+"</p>");
            $("#message").append("<p>"+text+"</p>");
        }
        if(roll)
        {
            document.getElementsByTagName('BODY')[0].scrollTop=document.getElementsByTagName('BODY')[0].scrollHeight;
        }
    });
}
function send()
{
    var text = $("#text").val();
    var name = $("#name").val();
    var time = new Date().getTime();
    $("#text").val("");
    $.post("send/",{"name":name,"text":text,"time":time},function(data,status){
        $("#time").text(data);
    });
}