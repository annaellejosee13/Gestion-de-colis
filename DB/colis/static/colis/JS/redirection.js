document.getElementById("redirectSelect").addEventListener("change", function()
{
        var selectedOption = this.value;
        if(selectedOption ){
            window.location.href = selectedOption;
        }
});