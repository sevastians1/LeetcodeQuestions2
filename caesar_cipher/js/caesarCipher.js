exports.caesarCipher = function(string, shift_amount) {
let answerString=[]
let newArr=string.split("")
for (let i=0; i<newArr.length; i++){
    let is_uppercase =false
    let x=newArr[i]
    if (newArr[i].replace(/[^a-zA-Z]+/,"DID")!=="DID")
        {
        // console.log(x)
        if (newArr[i]!==newArr[i].toLowerCase()){
            is_uppercase=true
        }
        x=x.toLowerCase()
        x=x.charCodeAt()
        x+=shift_amount
        if (x<97){
            x=123+(x-97)}
        else if (x>122){
            x=96+(x-122)}
        x=String.fromCharCode(x)
        // console.log(x, "THIS IS CHANGED")
        if (is_uppercase===true){
            x=x.toUpperCase()
        }
        // console.log(x, "final")
        }
    answerString.push(x)
    // console.log(newArr[i])
}
return answerString.join("")
};
// console.log((caesarCipher("ABC DEFGHIJKLMNOPQURSTUVWXYZ", 5))) 
// "Wjt! Rcvo v nomdib!"