
// Objects
let my_object = {
    my_property_1: "I'm an object.",
    my_property_2: {
        my_property_1: "I'm a nested object.",
    },
    my_function_1: function() {
        return this.my_property_1 + ' ' + this.my_property_2.my_property_1;
    },
    // Shorthand method syntax.
    what_am_i() {
        return this.my_property_1;
    },
}

console.log(my_object.my_function_1())
console.log(my_object.my_property_1);

let my_handler = {
    get(target, prop) {
        console.log(`Intercepted ${target} access to ${prop}.`);
        return target[prop];
    },
}

let my_object_2 = {
    my_property_1: "I'm also an object.",
    my_handler, // This refers to my_handler in enclosing scope.
}

const proxy = new Proxy(my_object_2, my_handler);

console.log(my_object_2.my_property_1);
console.log(my_handler.get(my_object_2, 'my_property_1'));
console.log(my_object_2.my_handler.get(my_object_2, 'my_property_1'));
console.log(proxy.my_property_1);
console.log(proxy['my_property_1']);
// console.log(proxy.my_handler);

// Note: classes are not hoisted.
class MyClass {
    static my_static_field = 'This is my static field.';
    static my_static_pi;
    static instance_count;

    static my_static_method() {
        return 'This is my static method.';
    }

    static {
        this.my_static_pi = 3.14;
        this.instance_count = 0;
        console.log('Initialized static things in this MyClass.');
    }
    
    my_field_2 = 'This is my field 2.';
    #my_field_1 = 'This is my field 1.';
    #is_disposed = false;

    constructor() {
        this.#my_field_1 = 'I assigned this again on construction.';
        this.my_field_3 = 'I was added during construction.';
        this.instance_count++;

        // It is recommended not to return anything from constructor.
    }

    dispose() {
        // Warning: this must be called manually when an object is going to be garbage collected.
        if (!this.#is_disposed) {
            this.#is_disposed = true;
            this.instance_count--;
        }
    }

    my_method() {
        return 'This is my method.';
    }

    get_my_field_1() {
        return this.#my_field_1;
    }

    get my_field_1() {
        return this.#my_field_1;
    }

    set my_field_1(value) {
        this.#my_field_1 = value;
    }
}

// Initializes static things.
console.log(MyClass.my_static_pi);

// If this became before MyClass.my_static_pi access above, the static things would be initialized here.
const my_class = new MyClass();

// Doesn't initialize static things since first construction already did.
const my_class_2 = new MyClass();

console.log(my_class.get_my_field_1());
console.log(my_class.my_field_3);

my_class.my_field_1 = 'I was set with a setter.';
console.log(`Gotten with a getter: ${my_class.my_field_1}`);


class MyClass2 extends MyClass {
    my_field_4;
    
    constructor(in_my_field_4) {
        super(); // Must call this in constructor before 'this' can be accessed.
        this.my_field_4 = in_my_field_4;
        // this.#my_field_1 = 'I am only accessible in super.'; // Note: only super's public members are accessible in derived classes.
    }
}

const my_class_2_1 = new MyClass2('This is my MyClass2 field.');

// Note: MyClass2 still has private members from super, but they're only accessible through public means outside of MyClass declaration.
console.log(my_class_2_1.my_field_1);


console.log(MyClass);
console.log(my_class_2);
console.log(my_class_2_1);

console.log(Object.prototype);
console.log(MyClass.prototype);
console.log(MyClass2.prototype);

my_class.dispose();
my_class_2.dispose();
my_class_2_1.dispose();