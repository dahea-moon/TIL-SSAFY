function a(x, y) {
    return x+y;
}

function b(n) {
    return n++; // return 하고 나서 n += 1
    // return ++n; // n+=1 하고 return
}

function c(f1, f2) {
    console.log(f1(10, 10))
    console.log(f2(99))
    return f1(10, 10) + f2(99)
}

console.log(
    c(a, b)
)