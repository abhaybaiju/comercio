import React from 'react'
import { AppBar, Grid, Typography, Container, Button} from '@material-ui/core';
import './Landing.css';
import LandingSVG from '../investsvg.svg';
function Landing() {
    
    const str = "easy";

    return (
        <div>
            <Container >
            <div class="custom-shape-divider-bottom-1599906837">
    <svg data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" preserveAspectRatio="none">
        <path d="M985.66,92.83C906.67,72,823.78,31,743.84,14.19c-82.26-17.34-168.06-16.33-250.45.39-57.84,11.73-114,31.07-172,41.86A600.21,600.21,0,0,1,0,27.35V120H1200V95.8C1132.19,118.92,1055.71,111.31,985.66,92.83Z" class="shape-fill"></path>
    </svg>
</div>
                <Grid spacing={9} direction="row" container alignItems="center" justify="center" style={{ minHeight: '100vh'}}>
                    <Grid item lg={7}>
                        <Typography variant="h1" component="h2" gutterBottom>
                            Investing is {str}
                        </Typography>
                        <Button variant="contained" color="primary" href="dashboard" size="large">Get Started</Button>
                    </Grid>
                    <Grid item lg={5}>
                        <Grid>
                            <img src={LandingSVG} width="500vh" ></img>
                        </Grid>
                    </Grid>
                </Grid>
            </Container>
        </div>
    )
}

export default Landing;
