//
//  GestureLockViewController.m
//  appForUITest
//
//  Created by hengjie chen on 27/6/2016.
//  Copyright © 2016 hengjie chen. All rights reserved.
//

#import "GestureLockViewController.h"
#import "DBGuestureLock.h"


@interface GestureLockViewController ()
{

}
@end

@implementation GestureLockViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view.
    [DBGuestureLock clearGuestureLockPassword]; //just for test
    
    //Give me a Star: https://github.com/i36lib/DBGuestureLock/
    
    //Working with delegate:
    //DBGuestureLock *lock = [DBGuestureLock lockOnView:self.view delegate:self];
    
    //Working with block:
    DBGuestureLock *lock = [DBGuestureLock lockOnView:self.view onPasswordSet:^(DBGuestureLock *lock, NSString *password) {
        if (lock.firstTimeSetupPassword == nil) {
            lock.firstTimeSetupPassword = password;
            NSLog(@"varify your password");
            self.label.text = @"Enter your password again:";
        }
    } onGetCorrectPswd:^(DBGuestureLock *lock, NSString *password) {
        if (lock.firstTimeSetupPassword && ![lock.firstTimeSetupPassword isEqualToString:DBFirstTimeSetupPassword]) {
            lock.firstTimeSetupPassword = DBFirstTimeSetupPassword;
            NSLog(@"password has been setup!");
            self.label.text = @"password has been setup!";
        } else {
            NSLog(@"login success");
            self.label.text = @"login success!";
        }
    } onGetIncorrectPswd:^(DBGuestureLock *lock, NSString *password) {
        if (![lock.firstTimeSetupPassword isEqualToString:DBFirstTimeSetupPassword]) {
            NSLog(@"Error: password not equal to first setup!");
            self.label.text = @"Not equal to first setup!";
        } else {
            NSLog(@"login failed");
            self.label.text = @"login failed!";
        }
    }];
    
    [self.view addSubview:lock];
    
    self.label.text = @"Please set your password:"; //for test
    [self.view setBackgroundColor:[UIColor colorWithRed:0.133 green:0.596 blue:0.933 alpha:1.00]];
}



- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

/*
#pragma mark - Navigation

// In a storyboard-based application, you will often want to do a little preparation before navigation
- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender {
    // Get the new view controller using [segue destinationViewController].
    // Pass the selected object to the new view controller.
}
*/

@end
