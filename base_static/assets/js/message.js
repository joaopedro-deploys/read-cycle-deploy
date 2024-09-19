(function remove(){
    const close_btn = document.querySelector('.btn-close')
    const error_div =  document.querySelector('.msg-container')
    close_btn.addEventListener('click', () => remove_div())
    setTimeout(() => {
        remove_msg_error()
        console.log('removeu')
    }, 3000)
   
    function remove_div(){
        if (error_div) {
            error_div.remove()
        }
    
     }
    }
)()   




