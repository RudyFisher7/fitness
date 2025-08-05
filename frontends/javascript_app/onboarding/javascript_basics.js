// Single line comment
/*
 * Multi-line comment
 */

// Variables
let my_var_1 = 1;
var my_var_2 = {
    my_var_2_property: 2,
    my_var_2_function_1: function(value) {
        return value + this.my_var_2_property;
    },
    my_var_2_function_2: function(value) {
        return value - this.my_var_2_property;
    },
};

const MY_PI_CONSTANT = 3.14;
const MY_OBJECT_CONSTANT = {
    property: 'mutate me if you want' // Properties of consts can be mutated.
};

const { my_var_2_property } = my_var_2; // Destructuring
console.log(`my_var_2_property: ${my_var_2_property} == my_var_2.my_var_2_property: ${my_var_2.my_var_2_property} == my_var_2['my_var_2_property']: ${my_var_2['my_var_2_property']}`);

// Scopes

// Global scope - available throughout this script.
var my_global_var_1 = 0;
let my_global_var_2 = 1;

function my_global_function() {
    // Local scope - available only in this function.
    var my_local_var_1 = 0;
    let my_local_var_2 = 1;

    if (true) {
        // Block scope - let and const only available in this block.
        var my_block_var_1 = 'block var 1';
        let my_block_var_2 = 1;
        const MY_BLOCK_CONSTANT = 2;
    }
    
    console.log(my_block_var_1); // This works.
}

// console.log(my_block_var_1); // This doesn't work.

console.log(my_hoisted_var_1); // Undefined, but it does exist (not recommended for variables).
var my_hoisted_var_1 = "Like all vars, I'm hoisted.";
console.log(my_hoisted_var_1); // Defined

my_hoisted_function(); // Hoisted entirely.
function my_hoisted_function() {
    console.log("Like all functions, I'm a hoisted function.");
}

// Global this has global variables.
// console.log(globalThis);

// Data types
// Variables can change their types whenever by assigning values of different types to them.
let my_bool = true;
let my_null = null;
let my_undefined = undefined;
let my_number_1 = 1;
let my_number_2 = 1.0;
let my_big_int = 90001n;
let my_string = "I'm a string.";
let my_symbol = Symbol('my_symbol');
let my_object = {
    property_1: 1,
    property_2: 1, // Trailing comma. Nice for git diffs with multi-line code.
};

let my_array = [1, 2, 3.14, /* emtpy item */ , my_bool, 'a string'];

let my_first_class_function = my_global_function;