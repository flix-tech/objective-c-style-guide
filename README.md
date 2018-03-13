These guidelines build on Apple's existing [Coding Guidelines for Cocoa](https://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/CodingGuidelines/CodingGuidelines.html).
Unless explicitly contradicted below, assume that all of Apple's guidelines apply as well.

## Whitespace

 * Spaces, not tabs.
 * End files with a newline.
 * Make liberal use of vertical whitespace to divide code into logical chunks.
 * Don’t leave trailing whitespace.
    * Not even leading indentation on blank lines.

## Documentation and Organization

 * All method declarations should be documented.
 * Comments should be hard-wrapped at 80 characters.
 * Comments should be [AppleDoc](https://github.com/tomaz/appledoc)-style.
 * Use Objective-C [nullability annotations](https://developer.apple.com/swift/blog/?id=25) to document nullability
 * Use Objective-C generics, especially in API definitions
 * Use `#pragma mark`s to categorize methods into functional groupings and protocol implementations, following this general structure:

```objc
#pragma mark Properties

@dynamic someProperty;

- (void)setCustomProperty:(id)value {}

#pragma mark Lifecycle

+ (instancetype)objectWithThing:(id)thing {}
- (instancetype)init {}

#pragma mark Drawing

- (void)drawRect:(CGRect) {}

#pragma mark Another functional grouping

#pragma mark GHSuperclass

- (void)someOverriddenMethod {}

#pragma mark NSCopying

- (id)copyWithZone:(NSZone *)zone {}

#pragma mark NSObject

- (NSString *)description {}
```

## Declarations

 * Prefer exposing an immutable type for a property if it being mutable is an implementation detail.
 * Declare memory-management semantics if and only if it differs from default (`assign` for primitives, `strong` for objects)
 * Declare properties `readonly` if they are only set once in `-init`.
 * Don't use `@synthesize` unless the compiler requires it. Note that optional properties in protocols must be explicitly synthesized in order to exist.
 * Instance variables should be prefixed with an underscore (just like when implicitly synthesized).
 * Don't put a space between an object type and the protocol it conforms to.

```objc
@property (attributes) id<Protocol> object;
@property (nonatomic) NSObject<Protocol> *object;
```

 * C function declarations should have no space before the opening parenthesis, and should be namespaced just like a class.

```objc
void GHAwesomeFunction(BOOL hasSomeArgs);
```

 * Constructors should generally return [`instancetype`](http://clang.llvm.org/docs/LanguageExtensions.html#related-result-types) rather than `id`.
 * Prefer helper functions (such as `CGRectMake()`) to C99 struct initialiser syntax.

```objc
  CGRect rect = CGRectMake(3.0, 12.0, 15.0, 80.0);
```

## Expressions

 * Use object literals, boxed expressions, and subscripting over the older, grosser alternatives.
 * Comparisons should be explicit for everything except `BOOL`s and object references in conditions.
 * Prefer positive comparisons to negative.
 * Long form ternary operators should be wrapped in parentheses and only used for assignment and arguments.

```objc
Blah *a = (stuff == thing ? foo : bar);
```

 * Short form, `nil` coalescing ternary operators should avoid parentheses.

```objc
Blah *b = thingThatCouldBeNil ?: defaultValue;
```

 * Separate binary operands and casts with a single space, but unary operands with none:

```c
void *ptr = &value + 10 * 3;
NewType a = (NewType) b;

for (int i = 0; i < 10; i++) {
    doCoolThings();
}
```

## Control Structures

 * Always surround `if`, `for`, `do`, `while` & `switch` bodies with curly braces.
 * All curly braces should begin on the same line as their associated statement. They should end on a new line.
 * Put a single space after keywords and before their parentheses.
 * Return and break early.
 * No spaces between parentheses and their contents.

```objc
if (somethingIsBad) {
  return;
}

if (!something) {
	// do stuff
} else {
	// do other stuff
}
```

## Exceptions and Error Handling

 * Don't use exceptions for flow control.
 * Use exceptions only to indicate programmer error.
 * To indicate errors, use an `NSError **` argument.

## Blocks

 * Blocks should have a space between their return type and name.
 * Block definitions should omit their return type when possible.
 * Block definitions should omit their arguments if they are `void`.
 * Parameters in block types should be named unless the block is initialized immediately.
 * Reused blocks should have `typedef`ed name.

```objc
void (^blockName1)(void) = ^{
    // do some things
};

id (^blockName2)(id) = ^id(id args) {
    // do some things
};
```

## Literals

 * The contents of array and dictionary literals should have a space on both sides.
 * Dictionary literals should have space between the key and the colon, and a single space between colon and value.

``` objc
NSArray *theStuff = @[ @1, @2, @3 ];

NSDictionary *keyedStuff = @{ GHDidCreateStyleGuide : @YES };
```

 * Longer or more complex literals should be split over multiple lines with a trailing comma (it helps to reduce the amount of VCS noise by making it possible to add new lines without changing existing ones):

``` objc
NSArray *theStuff = @[
    @"Got some long string objects in here.",
    [AndSomeModelObjects too],
    @"Moar strings.",
];

NSDictionary *keyedStuff = @{
    @"this.key" : @"corresponds to this value",
    @"otherKey" : @"remoteData.payload",
    @"some" : @"more",
    @"JSON" : @"keys",
    @"and" : @"stuff",
};
```

## Categories

 * Categories should be named for the sort of functionality they provide. Don't create umbrella categories.
 * Category methods should always be prefixed for 3rd party classes (i.e. for classes from Apple & 3rd party frameworks):
 
```objc
@interface UIColor (MFBRGB)

+ (instancetype)mfb_colorWithRed:(uint8_t)red green:(uint8_t)green blue:(uint8_t)blue;

@end
```
 
 * If you need to expose private methods for subclasses or unit testing, create a class extension named `Class+Private`.

## Protocol Implementation

 * Avoid name collision between protocols and classes implementing protocols.

## Nullability

 * Always wrap contents of header files in `NS_ASSUME_NONNULL_BEGIN`/`NS_ASSUME_NONNULL_END`.
 * Using nullability in implementation files is up to you, but is encouraged.
 * Always wrap contents of implementation files in `NS_ASSUME_NONNULL_BEGIN`/`NS_ASSUME_NONNULL_END` if nullability is used across the file.
 * Never use `nonnull` or `_Nonnull` explicitly because there's a macro wrapping.
 * Always use pretty version of nullability annotations whenever possible. Fallback to `_Nullable` etc. if and only if
it's not possible to use nicer version.

```objc
#import <Foundation/Foundation.h>

NS_ASSUME_NONNULL_BEGIN

@interface MeinFernbusAPI : NSObject

@property (nonatomic, nullable, readonly) NSURL *hostURL;

@end

NS_ASSUME_NONNULL_END
```

## Tests

 * XCTest framework with OCMock (for mocking) should be used. Manual mocking is also possible when appropriate.
 * When writing equality assertions, always pass actual value as a first argument and expected value as a second.
 * Always define mock objects as `id`, because types like `OCMockObject <ProtocolToMock> *` look overloaded and it's not always possible to declare the right type (i.e. when you're mocking a class, not protocol).
 * Try to avoid `andDo` while using mocks because using `NSInvocation` is error-prone. Consider using `andCall` or `+[OCMArg checkWithBlock:]` instead.
 * Name test methods using following template: `test_<#method name or alias#>_<#conditions#>_<#expected outcome#>`.
Use alias if the actual method name is too bulky. For simple tests without important preconditons and with obvious outcome (like JSON deserialization, for example) use simpler template: `test_<#method name or alias>`.
 * Always capitalize conditions & outcomes: `test_fetchJSON_NetworkAvailable_DeserializesObjects`.
 * Coalesce multiple test case conditions or outcomes with `And`: `test_fetchJSON_NetworkAvailableAndNotOfflineMode_DownloadsWithHTTPClientAndDeserializes`.

## clang-format

Provided [clang-format](clang-format) file is ready to use with clang-format and corresponding Xcode plugins.

It's recommended to add this repo as a submodule and make a symlink:

```bash
$ git submodule add git@github.com:flix-tech/objective-c-style-guide.git code-style
$ ln -s code-style/clang-format .clang-format
```
