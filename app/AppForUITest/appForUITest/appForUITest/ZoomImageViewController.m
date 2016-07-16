//
//  ZoomImageViewController.m
//  appForUITest
//
//  Created by hengjie chen on 29/6/2016.
//  Copyright © 2016 hengjie chen. All rights reserved.
//

#import "ZoomImageViewController.h"

@interface ZoomImageViewController ()

@property UIImageView *largeImageView;

@end

@implementation ZoomImageViewController 

-(void) viewDidLoad
{
    [super viewDidLoad];
    
    CGRect scrollFrame = CGRectMake(20, 90, 300, 300);
    
    // Create the UIScrollView to have the size of the window, matching its size
    UIScrollView *scrollView = [[UIScrollView alloc] initWithFrame:scrollFrame];
    scrollView.minimumZoomScale = 0.5;
    scrollView.maximumZoomScale = 200.0;
    scrollView.delegate = self;
    
    UIImage *bigImage = [UIImage imageNamed:@"photo.jpg"];
    self.largeImageView = [[UIImageView alloc] initWithImage:bigImage];
    
    // Tell the scrollView how big its subview is
    scrollView.contentSize = self.largeImageView.frame.size;   // Important
    scrollView.accessibilityLabel = @"imageScrollView";
    scrollView.isAccessibilityElement = YES;
    
    [scrollView addSubview:self.largeImageView];
    
    [self.view addSubview:scrollView];
}


- (UIView *)viewForZoomingInScrollView:(UIScrollView *)scrollView
{
    return self.largeImageView;
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
