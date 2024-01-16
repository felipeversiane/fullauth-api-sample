import React, { ReactNode } from 'react'
import Head from 'next/head'
import Footer from '../components/common/Footer'
import Header from '../components/common/Header'
import Provider from '../redux/provider'


type Props = {
  children?: ReactNode
  title?: string
}

export default function MainLayout({ children, title = 'Title' }: Props){
  return (
  <>
    <Head>
      <title>
        {title}
      </title>
      <meta charSet="utf-8" />
      <meta name="viewport" content="initial-scale=1.0, width=device-width" />
    </Head>
    <Provider>
    <Header/>
    {children}
    <Footer/>
    </Provider>
  </>
);
};
