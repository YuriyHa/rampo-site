url_url_regex=[/( https?:\/\/[^\s]+)/g, /(^https?:\/\/[^\s]+)/g]; 
url_img_regex=[/(img?:https:\/\/[^\s]+)/gm, /(img?:http:\/\/[^\s]+)/gm]
function urlify(text) {
    let context=text; 
    for(var i =0;i<url_url_regex.length;i++){ var urlRegex = url_url_regex[i];
        context=context.replace(urlRegex, function(url) {
            console.log(url); 
          return '<a href="' + url + '">' + url + '</a>';
        }); 
    }
    return context; 
} 
function imgify(text){
    let context=text;  
    for(var i=0;i<url_img_regex.length;i++){ var regex=url_img_regex[i]; 
        context=context.replace(regex, function(img_url) {
            url=img_url.replace(/img?:/, ""); 
            return '<img src="' + url + '">';
        })
    }
    return context; 
}
function h1fy(text){
    return text.replace(/<<<(.*)>>>/gm, function(fuck){
        return fuck.replace("<<<", '<h1>').replace(">>>", '</h1>');
    });
} 
document.body.onload=messageToLink; 
function messageToLink (argument) {
    messages =document.querySelectorAll(".message-text-hey"); 
    for (var mesid =0; mesid < messages.length; mesid++){
        messages[mesid].innerHTML=h1fy(messages[mesid].textContent); 
        messages[mesid].innerHTML=imgify(messages[mesid].innerHTML); 
        messages[mesid].innerHTML=urlify(messages[mesid].innerHTML);
    }
}